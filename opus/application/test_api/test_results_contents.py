# opus/application/test_api/test_results_contents.py

import json
import logging
import requests
from unittest import TestCase

from django.core.cache import cache
from rest_framework.test import RequestsClient

from api_test_helper import ApiTestHelper

import settings

class ApiResultsTests(TestCase, ApiTestHelper):

    def setUp(self):
        self.UPDATE_FILES = False
        self.maxDiff = None
        settings.OPUS_FAKE_API_DELAYS = 0
        settings.OPUS_FAKE_SERVER_ERROR404_PROBABILITY = 0
        settings.OPUS_FAKE_SERVER_ERROR500_PROBABILITY = 0
        settings.CACHE_KEY_PREFIX = 'opustest:' + settings.DB_SCHEMA_NAME
        logging.disable(logging.ERROR)
        if settings.TEST_GO_LIVE: # pragma: no cover
            self.client = requests.Session()
        else:
            self.client = RequestsClient()
        cache.clear()

    def tearDown(self):
        logging.disable(logging.NOTSET)


            #################################
            ######### RESULTS TESTS #########
            #################################

    def test__results_contents_co_cirs_0408010657_fp3_metadata(self):
        "[test_results_contents.py] co-cirs-0408010657-fp3 metadata"
        url = "/api/metadata_v2/co-cirs-0408010657-fp3.json"
        self._run_json_equal_file(url, "results_co_cirs_0408010657_fp3_metadata.json")

    def test__results_contents_co_cirs_0408010657_fp3_files(self):
        "[test_results_contents.py] co-cirs-0408010657-fp3 files"
        url = "/api/files/co-cirs-0408010657-fp3.json"
        self._run_json_equal_file(url, "results_co_cirs_0408010657_fp3_files.json")

    def test__results_contents_co_cirs_0408031652_fp1_metadata(self):
        "[test_results_contents.py] co-cirs-0408031652-fp1 metadata"
        url = "/api/metadata_v2/co-cirs-0408031652-fp1.json"
        self._run_json_equal_file(url, "results_co_cirs_0408031652_fp1_metadata.json")

    def test__results_contents_co_cirs_0408031652_fp1_files(self):
        "[test_results_contents.py] co-cirs-0408031652-fp1 files"
        url = "/api/files/co-cirs-0408031652-fp1.json"
        self._run_json_equal_file(url, "results_co_cirs_0408031652_fp1_files.json")

    def test__results_contents_co_cirs_0408041543_fp3_metadata(self):
        "[test_results_contents.py] co-cirs-0408041543-fp3 metadata"
        url = "/api/metadata_v2/co-cirs-0408041543-fp3.json"
        self._run_json_equal_file(url, "results_co_cirs_0408041543_fp3_metadata.json")

    def test__results_contents_co_cirs_0408041543_fp3_files(self):
        "[test_results_contents.py] co-cirs-0408041543-fp3 files"
        url = "/api/files/co-cirs-0408041543-fp3.json"
        self._run_json_equal_file(url, "results_co_cirs_0408041543_fp3_files.json")

    def test__results_contents_co_cirs_0408152208_fp3_metadata(self):
        "[test_results_contents.py] co-cirs-0408152208-fp3 metadata"
        url = "/api/metadata_v2/co-cirs-0408152208-fp3.json"
        self._run_json_equal_file(url, "results_co_cirs_0408152208_fp3_metadata.json")

    def test__results_contents_co_cirs_0408152208_fp3_files(self):
        "[test_results_contents.py] co-cirs-0408152208-fp3 files"
        url = "/api/files/co-cirs-0408152208-fp3.json"
        self._run_json_equal_file(url, "results_co_cirs_0408152208_fp3_files.json")

    def test__results_contents_co_cirs_0408161433_fp4_metadata(self):
        "[test_results_contents.py] co-cirs-0408161433-fp4 metadata"
        url = "/api/metadata_v2/co-cirs-0408161433-fp4.json"
        self._run_json_equal_file(url, "results_co_cirs_0408161433_fp4_metadata.json")

    def test__results_contents_co_cirs_0408161433_fp4_files(self):
        "[test_results_contents.py] co-cirs-0408161433-fp4 files"
        url = "/api/files/co-cirs-0408161433-fp4.json"
        self._run_json_equal_file(url, "results_co_cirs_0408161433_fp4_files.json")

    def test__results_contents_co_cirs_0408220524_fp4_metadata(self):
        "[test_results_contents.py] co-cirs-0408220524-fp4 metadata"
        url = "/api/metadata_v2/co-cirs-0408220524-fp4.json"
        self._run_json_equal_file(url, "results_co_cirs_0408220524_fp4_metadata.json")

    def test__results_contents_co_cirs_0408220524_fp4_files(self):
        "[test_results_contents.py] co-cirs-0408220524-fp4 files"
        url = "/api/files/co-cirs-0408220524-fp4.json"
        self._run_json_equal_file(url, "results_co_cirs_0408220524_fp4_files.json")

    def test__results_contents_co_iss_n1460961193_metadata(self):
        "[test_results_contents.py] co-iss-n1460961193 metadata"
        url = "/api/metadata_v2/co-iss-n1460961193.json"
        self._run_json_equal_file(url, "results_co_iss_n1460961193_metadata.json")

    def test__results_contents_co_iss_n1460961193_files(self):
        "[test_results_contents.py] co-iss-n1460961193 files"
        url = "/api/files/co-iss-n1460961193.json"
        self._run_json_equal_file(url, "results_co_iss_n1460961193_files.json")

    def test__results_contents_co_iss_n1461527506_metadata(self):
        "[test_results_contents.py] co-iss-n1461527506 metadata"
        url = "/api/metadata_v2/co-iss-n1461527506.json"
        self._run_json_equal_file(url, "results_co_iss_n1461527506_metadata.json")

    def test__results_contents_co_iss_n1461527506_files(self):
        "[test_results_contents.py] co-iss-n1461527506 files"
        url = "/api/files/co-iss-n1461527506.json"
        self._run_json_equal_file(url, "results_co_iss_n1461527506_files.json")

    def test__results_contents_co_iss_n1461810160_metadata(self):
        "[test_results_contents.py] co-iss-n1461810160 metadata"
        url = "/api/metadata_v2/co-iss-n1461810160.json"
        self._run_json_equal_file(url, "results_co_iss_n1461810160_metadata.json")

    def test__results_contents_co_iss_n1461810160_files(self):
        "[test_results_contents.py] co-iss-n1461810160 files"
        url = "/api/files/co-iss-n1461810160.json"
        self._run_json_equal_file(url, "results_co_iss_n1461810160_files.json")

    def test__results_contents_co_iss_n1462660850_metadata(self):
        "[test_results_contents.py] co-iss-n1462660850 metadata"
        url = "/api/metadata_v2/co-iss-n1462660850.json"
        self._run_json_equal_file(url, "results_co_iss_n1462660850_metadata.json")

    def test__results_contents_co_iss_n1462660850_files(self):
        "[test_results_contents.py] co-iss-n1462660850 files"
        url = "/api/files/co-iss-n1462660850.json"
        self._run_json_equal_file(url, "results_co_iss_n1462660850_files.json")

    def test__results_contents_co_iss_n1463306217_metadata(self):
        "[test_results_contents.py] co-iss-n1463306217 metadata"
        url = "/api/metadata_v2/co-iss-n1463306217.json"
        self._run_json_equal_file(url, "results_co_iss_n1463306217_metadata.json")

    def test__results_contents_co_iss_n1463306217_files(self):
        "[test_results_contents.py] co-iss-n1463306217 files"
        url = "/api/files/co-iss-n1463306217.json"
        self._run_json_equal_file(url, "results_co_iss_n1463306217_files.json")

    def test__results_contents_co_iss_n1481652288_metadata(self):
        "[test_results_contents.py] co-iss-n1481652288 metadata"
        url = "/api/metadata_v2/co-iss-n1481652288.json"
        self._run_json_equal_file(url, "results_co_iss_n1481652288_metadata.json")

    def test__results_contents_co_iss_n1481652288_files(self):
        "[test_results_contents.py] co-iss-n1481652288 files"
        url = "/api/files/co-iss-n1481652288.json"
        self._run_json_equal_file(url, "results_co_iss_n1481652288_files.json")

    def test__results_contents_co_iss_n1481663213_metadata(self):
        "[test_results_contents.py] co-iss-n1481663213 metadata"
        url = "/api/metadata_v2/co-iss-n1481663213.json"
        self._run_json_equal_file(url, "results_co_iss_n1481663213_metadata.json")

    def test__results_contents_co_iss_n1481663213_files(self):
        "[test_results_contents.py] co-iss-n1481663213 files"
        url = "/api/files/co-iss-n1481663213.json"
        self._run_json_equal_file(url, "results_co_iss_n1481663213_files.json")

    def test__results_contents_co_iss_n1481666413_metadata(self):
        "[test_results_contents.py] co-iss-n1481666413 metadata"
        url = "/api/metadata_v2/co-iss-n1481666413.json"
        self._run_json_equal_file(url, "results_co_iss_n1481666413_metadata.json")

    def test__results_contents_co_iss_n1481666413_files(self):
        "[test_results_contents.py] co-iss-n1481666413 files"
        url = "/api/files/co-iss-n1481666413.json"
        self._run_json_equal_file(url, "results_co_iss_n1481666413_files.json")

    def test__results_contents_co_iss_n1482859953_metadata(self):
        "[test_results_contents.py] co-iss-n1482859953 metadata"
        url = "/api/metadata_v2/co-iss-n1482859953.json"
        self._run_json_equal_file(url, "results_co_iss_n1482859953_metadata.json")

    def test__results_contents_co_iss_n1482859953_files(self):
        "[test_results_contents.py] co-iss-n1482859953 files"
        url = "/api/files/co-iss-n1482859953.json"
        self._run_json_equal_file(url, "results_co_iss_n1482859953_files.json")

    def test__results_contents_co_iss_w1481834905_metadata(self):
        "[test_results_contents.py] co-iss-w1481834905 metadata"
        url = "/api/metadata_v2/co-iss-w1481834905.json"
        self._run_json_equal_file(url, "results_co_iss_w1481834905_metadata.json")

    def test__results_contents_co_iss_w1481834905_files(self):
        "[test_results_contents.py] co-iss-w1481834905 files"
        url = "/api/files/co-iss-w1481834905.json"
        self._run_json_equal_file(url, "results_co_iss_w1481834905_files.json")

    def test__results_contents_co_uvis_euv2001_001_05_59_metadata(self):
        "[test_results_contents.py] co-uvis-euv2001_001_05_59 metadata"
        url = "/api/metadata_v2/co-uvis-euv2001_001_05_59.json"
        self._run_json_equal_file(url, "results_co_uvis_euv2001_001_05_59_metadata.json")

    def test__results_contents_co_uvis_euv2001_001_05_59_files(self):
        "[test_results_contents.py] co-uvis-euv2001_001_05_59 files"
        url = "/api/files/co-uvis-euv2001_001_05_59.json"
        self._run_json_equal_file(url, "results_co_uvis_euv2001_001_05_59_files.json")

    def test__results_contents_co_uvis_euv2001_002_12_27_metadata(self):
        "[test_results_contents.py] co-uvis-euv2001_002_12_27 metadata"
        url = "/api/metadata_v2/co-uvis-euv2001_002_12_27.json"
        self._run_json_equal_file(url, "results_co_uvis_euv2001_002_12_27_metadata.json")

    def test__results_contents_co_uvis_euv2001_002_12_27_files(self):
        "[test_results_contents.py] co-uvis-euv2001_002_12_27 files"
        url = "/api/files/co-uvis-euv2001_002_12_27.json"
        self._run_json_equal_file(url, "results_co_uvis_euv2001_002_12_27_files.json")

    def test__results_contents_co_uvis_euv2001_010_20_59_metadata(self):
        "[test_results_contents.py] co-uvis-euv2001_010_20_59 metadata"
        url = "/api/metadata_v2/co-uvis-euv2001_010_20_59.json"
        self._run_json_equal_file(url, "results_co_uvis_euv2001_010_20_59_metadata.json")

    def test__results_contents_co_uvis_euv2001_010_20_59_files(self):
        "[test_results_contents.py] co-uvis-euv2001_010_20_59 files"
        url = "/api/files/co-uvis-euv2001_010_20_59.json"
        self._run_json_equal_file(url, "results_co_uvis_euv2001_010_20_59_files.json")

    def test__results_contents_co_uvis_fuv2001_013_06_07_metadata(self):
        "[test_results_contents.py] co-uvis-fuv2001_013_06_07 metadata"
        url = "/api/metadata_v2/co-uvis-fuv2001_013_06_07.json"
        self._run_json_equal_file(url, "results_co_uvis_fuv2001_013_06_07_metadata.json")

    def test__results_contents_co_uvis_fuv2001_013_06_07_files(self):
        "[test_results_contents.py] co-uvis-fuv2001_013_06_07 files"
        url = "/api/files/co-uvis-fuv2001_013_06_07.json"
        self._run_json_equal_file(url, "results_co_uvis_fuv2001_013_06_07_files.json")

    def test__results_contents_co_uvis_hdac2001_022_04_45_metadata(self):
        "[test_results_contents.py] co-uvis-hdac2001_022_04_45 metadata"
        url = "/api/metadata_v2/co-uvis-hdac2001_022_04_45.json"
        self._run_json_equal_file(url, "results_co_uvis_hdac2001_022_04_45_metadata.json")

    def test__results_contents_co_uvis_hdac2001_022_04_45_files(self):
        "[test_results_contents.py] co-uvis-hdac2001_022_04_45 files"
        url = "/api/files/co-uvis-hdac2001_022_04_45.json"
        self._run_json_equal_file(url, "results_co_uvis_hdac2001_022_04_45_files.json")

    def test__results_contents_co_uvis_hsp2001_087_04_00_metadata(self):
        "[test_results_contents.py] co-uvis-hsp2001_087_04_00 metadata"
        url = "/api/metadata_v2/co-uvis-hsp2001_087_04_00.json"
        self._run_json_equal_file(url, "results_co_uvis_hsp2001_087_04_00_metadata.json")

    def test__results_contents_co_uvis_hsp2001_087_04_00_files(self):
        "[test_results_contents.py] co-uvis-hsp2001_087_04_00 files"
        url = "/api/files/co-uvis-hsp2001_087_04_00.json"
        self._run_json_equal_file(url, "results_co_uvis_hsp2001_087_04_00_files.json")

    def test__results_contents_co_vims_v1484504730_vis_metadata(self):
        "[test_results_contents.py] co-vims-v1484504730_vis metadata"
        url = "/api/metadata_v2/co-vims-v1484504730_vis.json"
        self._run_json_equal_file(url, "results_co_vims_v1484504730_vis_metadata.json")

    def test__results_contents_co_vims_v1484504730_vis_files(self):
        "[test_results_contents.py] co-vims-v1484504730_vis files"
        url = "/api/files/co-vims-v1484504730_vis.json"
        self._run_json_equal_file(url, "results_co_vims_v1484504730_vis_files.json")

    def test__results_contents_co_vims_v1484580518_vis_metadata(self):
        "[test_results_contents.py] co-vims-v1484580518_vis metadata"
        url = "/api/metadata_v2/co-vims-v1484580518_vis.json"
        self._run_json_equal_file(url, "results_co_vims_v1484580518_vis_metadata.json")

    def test__results_contents_co_vims_v1484580518_vis_files(self):
        "[test_results_contents.py] co-vims-v1484580518_vis files"
        url = "/api/files/co-vims-v1484580518_vis.json"
        self._run_json_equal_file(url, "results_co_vims_v1484580518_vis_files.json")

    def test__results_contents_co_vims_v1484860325_ir_metadata(self):
        "[test_results_contents.py] co-vims-v1484860325_ir metadata"
        url = "/api/metadata_v2/co-vims-v1484860325_ir.json"
        self._run_json_equal_file(url, "results_co_vims_v1484860325_ir_metadata.json")

    def test__results_contents_co_vims_v1484860325_ir_files(self):
        "[test_results_contents.py] co-vims-v1484860325_ir files"
        url = "/api/files/co-vims-v1484860325_ir.json"
        self._run_json_equal_file(url, "results_co_vims_v1484860325_ir_files.json")

    def test__results_contents_co_vims_v1485757341_ir_metadata(self):
        "[test_results_contents.py] co-vims-v1485757341_ir metadata"
        url = "/api/metadata_v2/co-vims-v1485757341_ir.json"
        self._run_json_equal_file(url, "results_co_vims_v1485757341_ir_metadata.json")

    def test__results_contents_co_vims_v1485757341_ir_files(self):
        "[test_results_contents.py] co-vims-v1485757341_ir files"
        url = "/api/files/co-vims-v1485757341_ir.json"
        self._run_json_equal_file(url, "results_co_vims_v1485757341_ir_files.json")

    def test__results_contents_co_vims_v1485803787_ir_metadata(self):
        "[test_results_contents.py] co-vims-v1485803787_ir metadata"
        url = "/api/metadata_v2/co-vims-v1485803787_ir.json"
        self._run_json_equal_file(url, "results_co_vims_v1485803787_ir_metadata.json")

    def test__results_contents_co_vims_v1485803787_ir_files(self):
        "[test_results_contents.py] co-vims-v1485803787_ir files"
        url = "/api/files/co-vims-v1485803787_ir.json"
        self._run_json_equal_file(url, "results_co_vims_v1485803787_ir_files.json")

    def test__results_contents_co_vims_v1487262184_ir_metadata(self):
        "[test_results_contents.py] co-vims-v1487262184_ir metadata"
        url = "/api/metadata_v2/co-vims-v1487262184_ir.json"
        self._run_json_equal_file(url, "results_co_vims_v1487262184_ir_metadata.json")

    def test__results_contents_co_vims_v1487262184_ir_files(self):
        "[test_results_contents.py] co-vims-v1487262184_ir files"
        url = "/api/files/co-vims-v1487262184_ir.json"
        self._run_json_equal_file(url, "results_co_vims_v1487262184_ir_files.json")

    def test__results_contents_co_vims_v1490874999_001_vis_metadata(self):
        "[test_results_contents.py] co-vims-v1490874999_001_vis metadata"
        url = "/api/metadata_v2/co-vims-v1490874999_001_vis.json"
        self._run_json_equal_file(url, "results_co_vims_v1490874999_001_vis_metadata.json")

    def test__results_contents_co_vims_v1490874999_001_vis_files(self):
        "[test_results_contents.py] co-vims-v1490874999_001_vis files"
        url = "/api/files/co-vims-v1490874999_001_vis.json"
        self._run_json_equal_file(url, "results_co_vims_v1490874999_001_vis_files.json")

    def test__results_contents_go_ssi_c0347769100_metadata(self):
        "[test_results_contents.py] go-ssi-c0347769100 metadata"
        url = "/api/metadata_v2/go-ssi-c0347769100.json"
        self._run_json_equal_file(url, "results_go_ssi_c0347769100_metadata.json")

    def test__results_contents_go_ssi_c0347769100_files(self):
        "[test_results_contents.py] go-ssi-c0347769100 files"
        url = "/api/files/go-ssi-c0347769100.json"
        self._run_json_equal_file(url, "results_go_ssi_c0347769100_files.json")

    def test__results_contents_go_ssi_c0349673988_metadata(self):
        "[test_results_contents.py] go-ssi-c0349673988 metadata"
        url = "/api/metadata_v2/go-ssi-c0349673988.json"
        self._run_json_equal_file(url, "results_go_ssi_c0349673988_metadata.json")

    def test__results_contents_go_ssi_c0349673988_files(self):
        "[test_results_contents.py] go-ssi-c0349673988 files"
        url = "/api/files/go-ssi-c0349673988.json"
        self._run_json_equal_file(url, "results_go_ssi_c0349673988_files.json")

    def test__results_contents_go_ssi_c0349761213_metadata(self):
        "[test_results_contents.py] go-ssi-c0349761213 metadata"
        url = "/api/metadata_v2/go-ssi-c0349761213.json"
        self._run_json_equal_file(url, "results_go_ssi_c0349761213_metadata.json")

    def test__results_contents_go_ssi_c0349761213_files(self):
        "[test_results_contents.py] go-ssi-c0349761213 files"
        url = "/api/files/go-ssi-c0349761213.json"
        self._run_json_equal_file(url, "results_go_ssi_c0349761213_files.json")

    def test__results_contents_go_ssi_c0359986600_metadata(self):
        "[test_results_contents.py] go-ssi-c0359986600 metadata"
        url = "/api/metadata_v2/go-ssi-c0359986600.json"
        self._run_json_equal_file(url, "results_go_ssi_c0359986600_metadata.json")

    def test__results_contents_go_ssi_c0359986600_files(self):
        "[test_results_contents.py] go-ssi-c0359986600 files"
        url = "/api/files/go-ssi-c0359986600.json"
        self._run_json_equal_file(url, "results_go_ssi_c0359986600_files.json")

    def test__results_contents_hst_05642_wfpc2_u2fi0c05t_metadata(self):
        "[test_results_contents.py] hst-05642-wfpc2-u2fi0c05t metadata"
        url = "/api/metadata_v2/hst-05642-wfpc2-u2fi0c05t.json"
        self._run_json_equal_file(url, "results_hst_05642_wfpc2_u2fi0c05t_metadata.json")

    def test__results_contents_hst_05642_wfpc2_u2fi0c05t_files(self):
        "[test_results_contents.py] hst-05642-wfpc2-u2fi0c05t files"
        url = "/api/files/hst-05642-wfpc2-u2fi0c05t.json"
        self._run_json_equal_file(url, "results_hst_05642_wfpc2_u2fi0c05t_files.json")

    def test__results_contents_hst_05642_wfpc2_u2fi0o0bt_metadata(self):
        "[test_results_contents.py] hst-05642-wfpc2-u2fi0o0bt metadata"
        url = "/api/metadata_v2/hst-05642-wfpc2-u2fi0o0bt.json"
        self._run_json_equal_file(url, "results_hst_05642_wfpc2_u2fi0o0bt_metadata.json")

    def test__results_contents_hst_05642_wfpc2_u2fi0o0bt_files(self):
        "[test_results_contents.py] hst-05642-wfpc2-u2fi0o0bt files"
        url = "/api/files/hst-05642-wfpc2-u2fi0o0bt.json"
        self._run_json_equal_file(url, "results_hst_05642_wfpc2_u2fi0o0bt_files.json")

    def test__results_contents_hst_05642_wfpc2_u2fi1901t_metadata(self):
        "[test_results_contents.py] hst-05642-wfpc2-u2fi1901t metadata"
        url = "/api/metadata_v2/hst-05642-wfpc2-u2fi1901t.json"
        self._run_json_equal_file(url, "results_hst_05642_wfpc2_u2fi1901t_metadata.json")

    def test__results_contents_hst_05642_wfpc2_u2fi1901t_files(self):
        "[test_results_contents.py] hst-05642-wfpc2-u2fi1901t files"
        url = "/api/files/hst-05642-wfpc2-u2fi1901t.json"
        self._run_json_equal_file(url, "results_hst_05642_wfpc2_u2fi1901t_files.json")

    def test__results_contents_hst_07181_nicmos_n4uc01b0q_metadata(self):
        "[test_results_contents.py] hst-07181-nicmos-n4uc01b0q metadata"
        url = "/api/metadata_v2/hst-07181-nicmos-n4uc01b0q.json"
        self._run_json_equal_file(url, "results_hst_07181_nicmos_n4uc01b0q_metadata.json")

    def test__results_contents_hst_07181_nicmos_n4uc01b0q_files(self):
        "[test_results_contents.py] hst-07181-nicmos-n4uc01b0q files"
        url = "/api/files/hst-07181-nicmos-n4uc01b0q.json"
        self._run_json_equal_file(url, "results_hst_07181_nicmos_n4uc01b0q_files.json")

    def test__results_contents_hst_07181_nicmos_n4uc01cjq_metadata(self):
        "[test_results_contents.py] hst-07181-nicmos-n4uc01cjq metadata"
        url = "/api/metadata_v2/hst-07181-nicmos-n4uc01cjq.json"
        self._run_json_equal_file(url, "results_hst_07181_nicmos_n4uc01cjq_metadata.json")

    def test__results_contents_hst_07181_nicmos_n4uc01cjq_files(self):
        "[test_results_contents.py] hst-07181-nicmos-n4uc01cjq files"
        url = "/api/files/hst-07181-nicmos-n4uc01cjq.json"
        self._run_json_equal_file(url, "results_hst_07181_nicmos_n4uc01cjq_files.json")

    def test__results_contents_hst_07316_stis_o57h02joq_metadata(self):
        "[test_results_contents.py] hst-07316-stis-o57h02joq metadata"
        url = "/api/metadata_v2/hst-07316-stis-o57h02joq.json"
        self._run_json_equal_file(url, "results_hst_07316_stis_o57h02joq_metadata.json")

    def test__results_contents_hst_07316_stis_o57h02joq_files(self):
        "[test_results_contents.py] hst-07316-stis-o57h02joq files"
        url = "/api/files/hst-07316-stis-o57h02joq.json"
        self._run_json_equal_file(url, "results_hst_07316_stis_o57h02joq_files.json")

    def test__results_contents_hst_07316_stis_o57h02010_metadata(self):
        "[test_results_contents.py] hst-07316-stis-o57h02010 metadata"
        url = "/api/metadata_v2/hst-07316-stis-o57h02010.json"
        self._run_json_equal_file(url, "results_hst_07316_stis_o57h02010_metadata.json")

    def test__results_contents_hst_07316_stis_o57h02010_files(self):
        "[test_results_contents.py] hst-07316-stis-o57h02010 files"
        url = "/api/files/hst-07316-stis-o57h02010.json"
        self._run_json_equal_file(url, "results_hst_07316_stis_o57h02010_files.json")

    def test__results_contents_hst_09975_acs_j8n460zvq_metadata(self):
        "[test_results_contents.py] hst-09975-acs-j8n460zvq metadata"
        url = "/api/metadata_v2/hst-09975-acs-j8n460zvq.json"
        self._run_json_equal_file(url, "results_hst_09975_acs_j8n460zvq_metadata.json")

    def test__results_contents_hst_09975_acs_j8n460zvq_files(self):
        "[test_results_contents.py] hst-09975-acs-j8n460zvq files"
        url = "/api/files/hst-09975-acs-j8n460zvq.json"
        self._run_json_equal_file(url, "results_hst_09975_acs_j8n460zvq_files.json")

    def test__results_contents_hst_11085_acs_j9xe05011_metadata(self):
        "[test_results_contents.py] hst-11085-acs-j9xe05011 metadata"
        url = "/api/metadata_v2/hst-11085-acs-j9xe05011.json"
        self._run_json_equal_file(url, "results_hst_11085_acs_j9xe05011_metadata.json")

    def test__results_contents_hst_11085_acs_j9xe05011_files(self):
        "[test_results_contents.py] hst-11085-acs-j9xe05011 files"
        url = "/api/files/hst-11085-acs-j9xe05011.json"
        self._run_json_equal_file(url, "results_hst_11085_acs_j9xe05011_files.json")

    def test__results_contents_hst_11559_wfc3_ib4v22gxq_metadata(self):
        "[test_results_contents.py] hst-11559-wfc3-ib4v22gxq metadata"
        url = "/api/metadata_v2/hst-11559-wfc3-ib4v22gxq.json"
        self._run_json_equal_file(url, "results_hst_11559_wfc3_ib4v22gxq_metadata.json")

    def test__results_contents_hst_11559_wfc3_ib4v22gxq_files(self):
        "[test_results_contents.py] hst-11559-wfc3-ib4v22gxq files"
        url = "/api/files/hst-11559-wfc3-ib4v22gxq.json"
        self._run_json_equal_file(url, "results_hst_11559_wfc3_ib4v22gxq_files.json")

    def test__results_contents_hst_13667_wfc3_icok28ihq_metadata(self):
        "[test_results_contents.py] hst-13667-wfc3-icok28ihq metadata"
        url = "/api/metadata_v2/hst-13667-wfc3-icok28ihq.json"
        self._run_json_equal_file(url, "results_hst_13667_wfc3_icok28ihq_metadata.json")

    def test__results_contents_hst_13667_wfc3_icok28ihq_files(self):
        "[test_results_contents.py] hst-13667-wfc3-icok28ihq files"
        url = "/api/files/hst-13667-wfc3-icok28ihq.json"
        self._run_json_equal_file(url, "results_hst_13667_wfc3_icok28ihq_files.json")

    def test__results_contents_hst_13667_wfc3_icok11rgq_metadata(self):
        "[test_results_contents.py] hst-13667-wfc3-icok11rgq metadata"
        url = "/api/metadata_v2/hst-13667-wfc3-icok11rgq.json"
        self._run_json_equal_file(url, "results_hst_13667_wfc3_icok11rgq_metadata.json")

    def test__results_contents_hst_13667_wfc3_icok11rgq_files(self):
        "[test_results_contents.py] hst-13667-wfc3-icok11rgq files"
        url = "/api/files/hst-13667-wfc3-icok11rgq.json"
        self._run_json_equal_file(url, "results_hst_13667_wfc3_icok11rgq_files.json")

    def test__results_contents_nh_lorri_lor_0299075349_metadata(self):
        "[test_results_contents.py] nh-lorri-lor_0299075349 metadata"
        url = "/api/metadata_v2/nh-lorri-lor_0299075349.json"
        self._run_json_equal_file(url, "results_nh_lorri_lor_0299075349_metadata.json")

    def test__results_contents_nh_lorri_lor_0299075349_files(self):
        "[test_results_contents.py] nh-lorri-lor_0299075349 files"
        url = "/api/files/nh-lorri-lor_0299075349.json"
        self._run_json_equal_file(url, "results_nh_lorri_lor_0299075349_files.json")

    def test__results_contents_nh_lorri_lor_0329817268_metadata(self):
        "[test_results_contents.py] nh-lorri-lor_0329817268 metadata"
        url = "/api/metadata_v2/nh-lorri-lor_0329817268.json"
        self._run_json_equal_file(url, "results_nh_lorri_lor_0329817268_metadata.json")

    def test__results_contents_nh_lorri_lor_0329817268_files(self):
        "[test_results_contents.py] nh-lorri-lor_0329817268 files"
        url = "/api/files/nh-lorri-lor_0329817268.json"
        self._run_json_equal_file(url, "results_nh_lorri_lor_0329817268_files.json")

    def test__results_contents_nh_lorri_lor_0330787458_metadata(self):
        "[test_results_contents.py] nh-lorri-lor_0330787458 metadata"
        url = "/api/metadata_v2/nh-lorri-lor_0330787458.json"
        self._run_json_equal_file(url, "results_nh_lorri_lor_0330787458_metadata.json")

    def test__results_contents_nh_lorri_lor_0330787458_files(self):
        "[test_results_contents.py] nh-lorri-lor_0330787458 files"
        url = "/api/files/nh-lorri-lor_0330787458.json"
        self._run_json_equal_file(url, "results_nh_lorri_lor_0330787458_files.json")

    def test__results_contents_nh_mvic_mc0_0032528036_metadata(self):
        "[test_results_contents.py] nh-mvic-mc0_0032528036 metadata"
        url = "/api/metadata_v2/nh-mvic-mc0_0032528036.json"
        self._run_json_equal_file(url, "results_nh_mvic_mc0_0032528036_metadata.json")

    def test__results_contents_nh_mvic_mc0_0032528036_files(self):
        "[test_results_contents.py] nh-mvic-mc0_0032528036 files"
        url = "/api/files/nh-mvic-mc0_0032528036.json"
        self._run_json_equal_file(url, "results_nh_mvic_mc0_0032528036_files.json")

    def test__results_contents_nh_mvic_mc1_0005261846_metadata(self):
        "[test_results_contents.py] nh-mvic-mc1_0005261846 metadata"
        url = "/api/metadata_v2/nh-mvic-mc1_0005261846.json"
        self._run_json_equal_file(url, "results_nh_mvic_mc1_0005261846_metadata.json")

    def test__results_contents_nh_mvic_mc1_0005261846_files(self):
        "[test_results_contents.py] nh-mvic-mc1_0005261846 files"
        url = "/api/files/nh-mvic-mc1_0005261846.json"
        self._run_json_equal_file(url, "results_nh_mvic_mc1_0005261846_files.json")

    def test__results_contents_nh_mvic_mp1_0012448104_metadata(self):
        "[test_results_contents.py] nh-mvic-mp1_0012448104 metadata"
        url = "/api/metadata_v2/nh-mvic-mp1_0012448104.json"
        self._run_json_equal_file(url, "results_nh_mvic_mp1_0012448104_metadata.json")

    def test__results_contents_nh_mvic_mp1_0012448104_files(self):
        "[test_results_contents.py] nh-mvic-mp1_0012448104 files"
        url = "/api/files/nh-mvic-mp1_0012448104.json"
        self._run_json_equal_file(url, "results_nh_mvic_mp1_0012448104_files.json")

    def test__results_contents_vg_iss_2_s_c4360353_metadata(self):
        "[test_results_contents.py] vg-iss-2-s-c4360353 metadata"
        url = "/api/metadata_v2/vg-iss-2-s-c4360353.json"
        self._run_json_equal_file(url, "results_vg_iss_2_s_c4360353_metadata.json")

    def test__results_contents_vg_iss_2_s_c4360353_files(self):
        "[test_results_contents.py] vg-iss-2-s-c4360353 files"
        url = "/api/files/vg-iss-2-s-c4360353.json"
        self._run_json_equal_file(url, "results_vg_iss_2_s_c4360353_files.json")

    def test__results_contents_mcd27m_iirar_occ_1989_184_28sgr_i_metadata(self):
        "[test_results_contents.py] mcd27m-iirar-occ-1989-184-28sgr-i metadata"
        url = "/api/metadata_v2/mcd27m-iirar-occ-1989-184-28sgr-i.json"
        self._run_json_equal_file(url, "results_mcd27m_iirar_occ_1989_184_28sgr_i_metadata.json")

    def test__results_contents_mcd27m_iirar_occ_1989_184_28sgr_i_files(self):
        "[test_results_contents.py] mcd27m-iirar-occ-1989-184-28sgr-i files"
        url = "/api/files/mcd27m-iirar-occ-1989-184-28sgr-i.json"
        self._run_json_equal_file(url, "results_mcd27m_iirar_occ_1989_184_28sgr_i_files.json")

    def test__results_contents_eso1m_apph_occ_1989_184_28sgr_e_metadata(self):
        "[test_results_contents.py] eso1m-apph-occ-1989-184-28sgr-e metadata"
        url = "/api/metadata_v2/eso1m-apph-occ-1989-184-28sgr-e.json"
        self._run_json_equal_file(url, "results_eso1m_apph_occ_1989_184_28sgr_e_metadata.json")

    def test__results_contents_eso1m_apph_occ_1989_184_28sgr_e_files(self):
        "[test_results_contents.py] eso1m-apph-occ-1989-184-28sgr-e files"
        url = "/api/files/eso1m-apph-occ-1989-184-28sgr-e.json"
        self._run_json_equal_file(url, "results_eso1m_apph_occ_1989_184_28sgr_e_files.json")

    def test__results_contents_lick1m_ccdc_occ_1989_184_28sgr_i_metadata(self):
        "[test_results_contents.py] lick1m-ccdc-occ-1989-184-28sgr-i metadata"
        url = "/api/metadata_v2/lick1m-ccdc-occ-1989-184-28sgr-i.json"
        self._run_json_equal_file(url, "results_lick1m_ccdc_occ_1989_184_28sgr_i_metadata.json")

    def test__results_contents_lick1m_ccdc_occ_1989_184_28sgr_i_files(self):
        "[test_results_contents.py] lick1m-ccdc-occ-1989-184-28sgr-i files"
        url = "/api/files/lick1m-ccdc-occ-1989-184-28sgr-i.json"
        self._run_json_equal_file(url, "results_lick1m_ccdc_occ_1989_184_28sgr_i_files.json")

    def test__results_contents_co_rss_occ_2005_123_rev007_k26_i_metadata(self):
        "[test_results_contents.py] co-rss-occ-2005-123-rev007-k26-i metadata"
        url = "/api/metadata_v2/co-rss-occ-2005-123-rev007-k26-i.json"
        self._run_json_equal_file(url, "results_co_rss_occ_2005_123_rev007_k26_i_metadata.json")

    def test__results_contents_co_rss_occ_2005_123_rev007_k26_i_files(self):
        "[test_results_contents.py] co-rss-occ-2005-123-rev007-k26-i files"
        url = "/api/files/co-rss-occ-2005-123-rev007-k26-i.json"
        self._run_json_equal_file(url, "results_co_rss_occ_2005_123_rev007_k26_i_files.json")

    def test__results_contents_co_rss_occ_2008_217_rev079c_s63_i_metadata(self):
        "[test_results_contents.py] co-rss-occ-2008-217-rev079c-s63-i metadata"
        url = "/api/metadata_v2/co-rss-occ-2008-217-rev079c-s63-i.json"
        self._run_json_equal_file(url, "results_co_rss_occ_2008_217_rev079c_s63_i_metadata.json")

    def test__results_contents_co_rss_occ_2008_217_rev079c_s63_i_files(self):
        "[test_results_contents.py] co-rss-occ-2008-217-rev079c-s63-i files"
        url = "/api/files/co-rss-occ-2008-217-rev079c-s63-i.json"
        self._run_json_equal_file(url, "results_co_rss_occ_2008_217_rev079c_s63_i_files.json")

    def test__results_contents_co_rss_occ_2010_170_rev133_x34_e_metadata(self):
        "[test_results_contents.py] co-rss-occ-2010-170-rev133-x34-e metadata"
        url = "/api/metadata_v2/co-rss-occ-2010-170-rev133-x34-e.json"
        self._run_json_equal_file(url, "results_co_rss_occ_2010_170_rev133_x34_e_metadata.json")

    def test__results_contents_co_rss_occ_2010_170_rev133_x34_e_files(self):
        "[test_results_contents.py] co-rss-occ-2010-170-rev133-x34-e files"
        url = "/api/files/co-rss-occ-2010-170-rev133-x34-e.json"
        self._run_json_equal_file(url, "results_co_rss_occ_2010_170_rev133_x34_e_files.json")

    def test__results_contents_co_uvis_occ_2005_139_126tau_e_metadata(self):
        "[test_results_contents.py] co-uvis-occ-2005-139-126tau-e metadata"
        url = "/api/metadata_v2/co-uvis-occ-2005-139-126tau-e.json"
        self._run_json_equal_file(url, "results_co_uvis_occ_2005_139_126tau_e_metadata.json")

    def test__results_contents_co_uvis_occ_2005_139_126tau_e_files(self):
        "[test_results_contents.py] co-uvis-occ-2005-139-126tau-e files"
        url = "/api/files/co-uvis-occ-2005-139-126tau-e.json"
        self._run_json_equal_file(url, "results_co_uvis_occ_2005_139_126tau_e_files.json")

    def test__results_contents_co_uvis_occ_2005_175_126tau_i_metadata(self):
        "[test_results_contents.py] co-uvis-occ-2005-175-126tau-i metadata"
        url = "/api/metadata_v2/co-uvis-occ-2005-175-126tau-i.json"
        self._run_json_equal_file(url, "results_co_uvis_occ_2005_175_126tau_i_metadata.json")

    def test__results_contents_co_uvis_occ_2005_175_126tau_i_files(self):
        "[test_results_contents.py] co-uvis-occ-2005-175-126tau-i files"
        url = "/api/files/co-uvis-occ-2005-175-126tau-i.json"
        self._run_json_equal_file(url, "results_co_uvis_occ_2005_175_126tau_i_files.json")

    def test__results_contents_co_uvis_occ_2009_015_gamcas_e_metadata(self):
        "[test_results_contents.py] co-uvis-occ-2009-015-gamcas-e metadata"
        url = "/api/metadata_v2/co-uvis-occ-2009-015-gamcas-e.json"
        self._run_json_equal_file(url, "results_co_uvis_occ_2009_015_gamcas_e_metadata.json")

    def test__results_contents_co_uvis_occ_2009_015_gamcas_e_files(self):
        "[test_results_contents.py] co-uvis-occ-2009-015-gamcas-e files"
        url = "/api/files/co-uvis-occ-2009-015-gamcas-e.json"
        self._run_json_equal_file(url, "results_co_uvis_occ_2009_015_gamcas_e_files.json")

    def test__results_contents_co_vims_occ_2006_204_alpori_i_metadata(self):
        "[test_results_contents.py] co-vims-occ-2006-204-alpori-i metadata"
        url = "/api/metadata_v2/co-vims-occ-2006-204-alpori-i.json"
        self._run_json_equal_file(url, "results_co_vims_occ_2006_204_alpori_i_metadata.json")

    def test__results_contents_co_vims_occ_2006_204_alpori_i_files(self):
        "[test_results_contents.py] co-vims-occ-2006-204-alpori-i files"
        url = "/api/files/co-vims-occ-2006-204-alpori-i.json"
        self._run_json_equal_file(url, "results_co_vims_occ_2006_204_alpori_i_files.json")

    def test__results_contents_co_vims_occ_2014_175_l2pup_e_metadata(self):
        "[test_results_contents.py] co-vims-occ-2014-175-l2pup-e metadata"
        url = "/api/metadata_v2/co-vims-occ-2014-175-l2pup-e.json"
        self._run_json_equal_file(url, "results_co_vims_occ_2014_175_l2pup_e_metadata.json")

    def test__results_contents_co_vims_occ_2014_175_l2pup_e_files(self):
        "[test_results_contents.py] co-vims-occ-2014-175-l2pup-e files"
        url = "/api/files/co-vims-occ-2014-175-l2pup-e.json"
        self._run_json_equal_file(url, "results_co_vims_occ_2014_175_l2pup_e_files.json")
