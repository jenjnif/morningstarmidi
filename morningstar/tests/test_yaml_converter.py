import unittest
from morningstar import yaml_converter
import os


class TestYamlConverter(unittest.TestCase):

    def test_blank_bank(self):
        # Checks that a blank YAML definition results in the same sysex as a blank bank exported from Morningstar editor
        blank_bank = {
            "name": None,
            'presets': None
        }
        data = yaml_converter.convert_to_bank(blank_bank).to_sysex()
        print(yaml_converter.format_data(data))

        self.assertEqual(data[0x00],
                         [0xF0, 0x00, 0x21, 0x24, 0x03, 0x03, 0x02, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x75, 0xF7])
        self.assertEqual(data[0x01],
                         [0xF0, 0x00, 0x21, 0x24, 0x03, 0x03, 0x01, 0x11, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x65, 0xF7])
        self.assertEqual(data[0x02],
                         [0xF0, 0x00, 0x21, 0x24, 0x03, 0x03, 0x01, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x72, 0xF7])
        self.assertEqual(data[0x03],
                         [0xF0, 0x00, 0x21, 0x24, 0x03, 0x03, 0x01, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59,
                          0x20, 0x20, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x73, 0xF7])
        self.assertEqual(data[0x04],
                         [0xF0, 0x00, 0x21, 0x24, 0x03, 0x03, 0x01, 0x07, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59,
                          0x20, 0x20, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x72, 0xF7])
        self.assertEqual(data[0x05],
                         [0xF0, 0x00, 0x21, 0x24, 0x03, 0x03, 0x01, 0x07, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59,
                          0x20, 0x20, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x71, 0xF7])
        self.assertEqual(data[0x06],
                         [0xF0, 0x00, 0x21, 0x24, 0x03, 0x03, 0x01, 0x07, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59,
                          0x20, 0x20, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x70, 0xF7])
        self.assertEqual(data[0x07],
                         [0xF0, 0x00, 0x21, 0x24, 0x03, 0x03, 0x01, 0x07, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59,
                          0x20, 0x20, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x77, 0xF7])
        self.assertEqual(data[0x08],
                         [0xF0, 0x00, 0x21, 0x24, 0x03, 0x03, 0x01, 0x07, 0x00, 0x05, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59,
                          0x20, 0x20, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x76, 0xF7])
        self.assertEqual(data[0x09],
                         [0xF0, 0x00, 0x21, 0x24, 0x03, 0x03, 0x01, 0x07, 0x00, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59,
                          0x20, 0x20, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x75, 0xF7])
        self.assertEqual(data[0x0A],
                         [0xF0, 0x00, 0x21, 0x24, 0x03, 0x03, 0x01, 0x07, 0x00, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59,
                          0x20, 0x20, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x74, 0xF7])
        self.assertEqual(data[0x0B],
                         [0xF0, 0x00, 0x21, 0x24, 0x03, 0x03, 0x01, 0x07, 0x00, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59,
                          0x20, 0x20, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x7B, 0xF7])
        self.assertEqual(data[0x0C],
                         [0xF0, 0x00, 0x21, 0x24, 0x03, 0x03, 0x01, 0x07, 0x00, 0x09, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59,
                          0x20, 0x20, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x7A, 0xF7])
        self.assertEqual(data[0x0D],
                         [0xF0, 0x00, 0x21, 0x24, 0x03, 0x03, 0x01, 0x07, 0x00, 0xA, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59, 0x20,
                          0x20, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x79, 0xF7])
        self.assertEqual(data[0x0E],
                         [0xF0, 0x00, 0x21, 0x24, 0x03, 0x03, 0x01, 0x07, 0x00, 0xB, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59, 0x20,
                          0x20, 0x20, 0x45, 0x4D, 0x50, 0x54, 0x59, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x78, 0xF7])
        self.assertEqual(data[0x0F],
                         [0xF0, 0x00, 0x21, 0x24, 0x03, 0x03, 0x01, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x45, 0x58, 0x50, 0x52, 0x4E,
                          0x20, 0x20, 0x20, 0x45, 0x58, 0x50, 0x52, 0x4E, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x7C, 0xF7])
        self.assertEqual(data[0x10],
                         [0xF0, 0x00, 0x21, 0x24, 0x03, 0x03, 0x01, 0x08, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x45, 0x58, 0x50, 0x52, 0x4E,
                          0x20, 0x20, 0x20, 0x45, 0x58, 0x50, 0x52, 0x4E, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
                          0x20, 0x20, 0x20, 0x20, 0x7D, 0xF7])
        self.assertEqual(data[0x11],
                         [0xF0, 0x00, 0x21, 0x24, 0x03, 0x03, 0x7E, 0x00, 0x13, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x18, 0xF7])

    def test_bank_name(self):
        named_bank = {
            "name": 'BANKNAMECANBEREALLYLOONG',
            'presets': None
        }
        data = yaml_converter.convert_to_bank(named_bank).to_sysex()
        self.assertEqual(data[0x02],
                         [0xF0, 0x00, 0x21, 0x24, 0x03, 0x03, 0x01, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x42, 0x41, 0x4E, 0x4B, 0x4E, 0x41, 0x4D, 0x45, 0x43, 0x41, 0x4E, 0x42,
                          0x45, 0x52, 0x45, 0x41, 0x4C, 0x4C, 0x59, 0x4C, 0x4F, 0x4F, 0x4E, 0x47, 0x72, 0xF7])

    def test_preset_names(self):
        named_preset_bank = {
            "presets": {
                "A": {
                    "name": "PRESET01",
                    "toggle_name": "TOGGLE01",
                    "long_name": "LONGNAMEFORPRESET0000001",
                }
            }
        }
        data = yaml_converter.convert_to_bank(named_preset_bank).to_sysex()
        self.assertEqual(data[0x03],
                         [0xF0, 0x00, 0x21, 0x24, 0x03, 0x03, 0x01, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x50, 0x52, 0x45, 0x53, 0x45, 0x54,
                          0x30, 0x31, 0x54, 0x4F, 0x47, 0x47, 0x4C, 0x45, 0x30, 0x31, 0x4C, 0x4F, 0x4E, 0x47, 0x4E,
                          0x41, 0x4D, 0x45, 0x46, 0x4F, 0x52, 0x50, 0x52, 0x45, 0x53, 0x45, 0x54, 0x30, 0x30, 0x30,
                          0x30, 0x30, 0x30, 0x31, 0x06, 0xF7])

    def test_actions(self):
        named_preset_bank = {
            "presets": {
                "A": {
                    "actions": [
                        {
                            "type": "press",
                            "channel": 2,
                            "messages": [{
                                "program_change": 1
                            }]
                        },
                        {
                            "type": "release",
                            "channel": 3,
                            "control_change": {
                                "number": 4,
                                "value": 5
                            }
                        }
                    ]
                }
            }
        }

        data = yaml_converter.convert_to_bank(named_preset_bank).to_sysex()
        self.assertEqual(data[0x03][16:22], [0x01, 0x01, 0x00, 0x00, 0x02, 0x01])
        self.assertEqual(data[0x03][22:28], [0x02, 0x04, 0x05, 0x00, 0x04, 0x02])

    def test_preset_bit_fields(self):
        data = yaml_converter.convert_to_bank({
            "presets": {
                "A": {
                    "toggle_mode": True,
                    "blink_mode": True
                }
            }
        }).to_sysex()
        self.assertEqual(data[0x03][0x70], 0x0C)

        data = yaml_converter.convert_to_bank({
            "presets": {
                "A": {
                    "toggle_mode": True,
                    "blink_mode": False
                }
            }
        }).to_sysex()
        self.assertEqual(data[0x03][0x70], 0x08)

        data = yaml_converter.convert_to_bank({
            "presets": {
                "A": {
                    "toggle_mode": False,
                    "blink_mode": True
                }
            }
        }).to_sysex()
        self.assertEqual(data[0x03][0x70], 0x04)

    def test_debug_yaml_matches_sysex(self):
        with open(os.path.dirname(__file__) + '/../../yaml/debug.yml', 'r') as input_file:
            with open('output.syx', 'w') as output_file:
                yaml_converter.main(input_file, output_file, False, 0)

        with open(os.path.dirname(__file__) + '/debug.syx', 'r') as expectationfile:
            expectation = expectationfile.readlines()
        with open('output.syx', 'r') as actualfile:
            actual = actualfile.readlines()

        for i, line in enumerate(expectation):
            print("Checking line " + str(i + 1))
            print("Expected : " + line[:-1])
            print("Generated: " + actual[i][:-1])
            self.assertEqual(actual[i], line)


if __name__ == "__main__":
    unittest.main()