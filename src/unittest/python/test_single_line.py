import sys
import string
import unittest
from mock import patch
from mock import Mock
from mock import call
from single_line import SingleLine


class TestSingleLine(unittest.TestCase):

    @patch('single_line.just_fix_windows_console')
    def test__init_Should_SetDefaults_When_Called(self, get_fill_patch, *patches):
        line = SingleLine()
        self.assertEqual(line.message_when_done, '')
        self.assertEqual(line.stream, sys.stdout)

    @patch('single_line.sys.stdout.isatty', return_value=True)
    @patch('single_line.SingleLine.print')
    @patch('single_line.print')
    @patch('single_line.cursor')
    def test__enter_exit_Should_HideAndShowCursor_When_Tty(self, cursor_patch, print_patch, line_print_patch, *patches):
        with SingleLine(message_when_done='done'):
            cursor_patch.hide.assert_called_once_with()
            print_patch.assert_called_once_with('')
        line_print_patch.assert_called_once_with('done')
        cursor_patch.show.assert_called_once_with()

    @patch('single_line.sys.stdout.isatty', return_value=True)
    @patch('single_line.Fore')
    @patch('single_line.Back')
    @patch('single_line.Style')
    @patch('single_line.Cursor')
    @patch('single_line.print')
    def test__print_Should_PrintMessage_When_Tty(self, print_patch, cursor_patch, *patches):
        line = SingleLine()
        line.print('message')
        self.assertEqual(len(print_patch.mock_calls), 2)
        mockstr = f'{cursor_patch.UP.return_value}{line.clear_eol}'
        self.assertTrue(call(mockstr, end='', file=line.stream) in print_patch.mock_calls)
