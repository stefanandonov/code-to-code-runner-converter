import json
import os
import getopt
import sys

from markdown2 import Markdown
from xml.dom import minidom

mark_downer = Markdown()


def create_test_case_XML(test_case, example=0):
    xml_testcase = ""
    xml_testcase += f"""      <testcase testtype="0" useasexample="%d" hiderestiffail="0" mark="1.0000000" >
      <testcode>
                <text></text>
      </testcode>
      <stdin>
                <text>""" % example
    xml_testcase += test_case['testCase.input']
    xml_testcase += """</text>
      </stdin>
      <expected>
                <text>"""

    xml_testcase += test_case['testCase.output']
    xml_testcase += """</text>
      </expected>
      <extra>
                <text></text>
      </extra>
      <display>
                <text>SHOW</text>
      </display>
    </testcase>"""

    return xml_testcase


def create_task_XML(data):
    xml_string = ""
    xml_string += "<question type=\"coderunner\">\n"

    xml_string += ("    <name>\n\t<text>" + data["problem.name"] + "</text>\n\t</name>\n")
    xml_string += "    <questiontext format=\"html\">\n\t<text><![CDATA["
    xml_string += mark_downer.convert(data['problem.text'])
    xml_string += """]]></text>
        </questiontext>
        <generalfeedback format=\"html\">
          <text></text>
        </generalfeedback>
        <defaultgrade>1.0000000</defaultgrade>
        <penalty>0.0000000</penalty>
        <hidden>0</hidden>
        <idnumber></idnumber>
        <coderunnertype>c_program_no_warning</coderunnertype>
        <prototypetype>0</prototypetype>
        <allornothing>0</allornothing>
        <penaltyregime>0</penaltyregime>
        <precheck>0</precheck>
        <showsource>0</showsource>
        <answerboxlines>18</answerboxlines>
        <answerboxcolumns>100</answerboxcolumns>
        <answerpreload></answerpreload>
        <globalextra></globalextra>
        <useace></useace>
        <resultcolumns></resultcolumns>
        <template></template>
        <iscombinatortemplate></iscombinatortemplate>
        <allowmultiplestdins></allowmultiplestdins>
        <answer><![CDATA["""

    xml_string += data['problem.problemData'][0]['problemData.solution']
    xml_string += "]]></answer>\n"
    xml_string += """    <validateonsave>1</validateonsave>
        <testsplitterre></testsplitterre>
        <language></language>
        <acelang></acelang>
        <sandbox></sandbox>
        <grader></grader>
        <cputimelimitsecs></cputimelimitsecs>
        <memlimitmb></memlimitmb>
        <sandboxparams></sandboxparams>
        <templateparams></templateparams>
        <hoisttemplateparams>1</hoisttemplateparams>
        <twigall>0</twigall>
        <uiplugin></uiplugin>
        <attachments>0</attachments>
        <attachmentsrequired>0</attachmentsrequired>
        <maxfilesize>10240</maxfilesize>
        <filenamesregex></filenamesregex>
        <filenamesexplain></filenamesexplain>
        <displayfeedback>1</displayfeedback>
        <testcases>"""

    for i, test_case in enumerate(data['problem.testCases']):
        if i == 0:
            xml_string += create_test_case_XML(test_case, 1)
        else:
            xml_string += create_test_case_XML(test_case)

    xml_string += """</testcases>
      </question>"""

    return xml_string


def load_json_from_file(file_path):
    json_file = open(file_path)
    return json.load(json_file)


def generate_xml_file_for_category(path, category):
    xml = ""
    xml += f"""<?xml version="1.0" encoding="UTF-8"?>
<quiz>
<!-- question: 0  -->
  <question type="category">
    <category>
      <text>%s</text>
    </category>
    <info format="moodle_auto_format">
      <text>CodeRunner questions exported from code.finki.ukim.mk for %s.</text>
    </info>
    <idnumber></idnumber>
  </question>""" % (category, category)
    for json_filename in os.listdir(path):
        if json_filename.endswith(".json"):
            task_xml = create_task_XML(load_json_from_file(path + "/" + json_filename))
            xml += task_xml
    xml += """</quiz>"""
    return xml


def main(argv):
    input_folder = ""
    output_folder = ""
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifolder=", "ofolder="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfolder> -o <outputfolrder>')
            sys.exit()
        elif opt in ("-i", "--ifolder"):
            input_folder = arg
        elif opt in ("-o", "--ofolder"):
            output_folder = arg
            if not (os.path.isdir(output_folder)):
                os.mkdir(output_folder)
    print(input_folder, output_folder)
    if len(input_folder) != 0 and len(output_folder) != 0:
        print("in here")
        for subdirectory in os.listdir(input_folder):
            if not (subdirectory.startswith(".")):
                xml = generate_xml_file_for_category(input_folder + "/" + subdirectory, subdirectory)
                file = open(output_folder + "/" + subdirectory + ".xml", "w")
                file.write(xml)
                file.close()


if __name__ == "__main__":
    main(sys.argv[1:])

