#!/usr/bin/env python2.7
"""
Initially Generated By:
    python -m utool --tf setup_repo --repo=pydarknet --codedir=~/code --modname=pydarknet
"""
from __future__ import absolute_import, division, print_function
import sys
import utool as ut


def run_tests():
    # # Build module list and run tests
    # import sys
    # ut.change_term_title('RUN pydarknet TESTS')
    # exclude_doctests_fnames = set([
    # ])
    # exclude_dirs = [
    #     '_broken', 'old', 'tests', 'timeits',
    #     '_scripts', '_timeits', '_doc', 'notebook',
    # ]
    # dpath_list = ['pydarknet']
    # doctest_modname_list = ut.find_doctestable_modnames(
    #     dpath_list, exclude_doctests_fnames, exclude_dirs)

    # for modname in doctest_modname_list:
    #     exec('import ' + modname, globals())
    # module_list = [sys.modules[name] for name in doctest_modname_list]
    # nPass, nTotal, failed_cmd_list = ut.doctest_module_list(module_list)
    # if nPass != nTotal:
    #     return 1
    # else:
    #     return 0

    from pydarknet import Darknet_YOLO_Detector

    # dark = Darknet_YOLO_Detector()
    # voc_path = '/media/hdd/jason/yolo/LearningData'
    # weight_path = '/media/hdd/jason/yolo/weights'
    # ut.ensuredir(weight_path)
    # dark.train(voc_path, weight_path)

    config_filepath = '/media/hdd/jason/yolo/weights/detect.yolo.12.cfg'
    weight_filepath = '/media/hdd/jason/yolo/weights/detect.yolo.12.40000.weights'
    # config_filepath = '/Users/bluemellophone/Desktop/detect.yolo.12.cfg'
    # weight_filepath = '/Users/bluemellophone/Desktop/detect.yolo.12.weights'
    dark = Darknet_YOLO_Detector(config_filepath=config_filepath, weight_filepath=weight_filepath)

    import cv2
    from os.path import abspath, join, basename
    input_gpath_list = [
        abspath(join('_test', 'test_%05d.jpg' % (i, )))
        for i in range(1, 76)
    ]
    # input_gpath_list = input_gpath_list[:2]

    temp_path = abspath('temp')
    ut.ensuredir(temp_path)

    results_list1 = list(dark.detect(input_gpath_list, grid=False))
    results_list2 = list(dark.detect(input_gpath_list, grid=True))

    zipped = zip(results_list1, results_list2)
    for (filename, result_list1), (filename2, result_list2) in zipped:
        print(filename)
        image = cv2.imread(filename)
        for result in result_list1:
            if result['confidence'] < 0.5:
                continue
            print('    Found 1: %r' % (result, ))
            xtl = int(result['xtl'])
            ytl = int(result['ytl'])
            xbr = int(result['xtl'] + result['width'])
            ybr = int(result['ytl'] + result['height'])
            cv2.rectangle(image, (xtl, ytl), (xbr, ybr), (255, 140, 0), 5)
        for result in result_list2:
            if result['confidence'] < 0.5:
                continue
            print('    Found 2: %r' % (result, ))
            xtl = int(result['xtl'])
            ytl = int(result['ytl'])
            xbr = int(result['xtl'] + result['width'])
            ybr = int(result['ytl'] + result['height'])
            cv2.rectangle(image, (xtl, ytl), (xbr, ybr), (0, 140, 255), 3)
        for result in result_list1:
            if result['confidence'] < 0.5:
                continue
            xtl = int(result['xtl'])
            ytl = int(result['ytl'])
            xbr = int(result['xtl'] + result['width'])
            ybr = int(result['ytl'] + result['height'])
            cv2.rectangle(image, (xtl, ytl), (xbr, ybr), (255, 140, 0), 1)
        temp_filepath = join(temp_path, basename(filename))
        cv2.imwrite(temp_filepath, image)


if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    retcode = run_tests()
    sys.exit(retcode)
