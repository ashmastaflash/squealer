class MarkDowner(object):
    def __init__(self):
        return

    @classmethod
    def translate_csm(cls, csm_scan):
        md_formatted = "## Configuration Scan Results:\n"
        critical_header = ("\n\n### Critical Finding!\n" +
                           "| Type | Expected | Actual | Target |\n" +
                           "|------|----------|--------|--------|\n")
        noncritical_header = ("\n\n### Noncritical Finding!\n" +
                              "| Type | Expected | Actual | Target |\n" +
                              "|------|----------|--------|--------|\n")
        findings = csm_scan["scan"]["findings"]
        for finding in findings:
            if finding["critical"] is True:
                md_formatted = md_formatted + critical_header
                md_formatted = md_formatted + MarkDowner.format_csm_finding_details(finding["details"])
            else:
                md_formatted = md_formatted + noncritical_header
                md_formatted = md_formatted + MarkDowner.format_csm_finding_details(finding["details"])
        return md_formatted

    @classmethod
    def format_csm_finding_details(cls, details):
        result = ""
        for detail in details:
            result = result + "| %s | %s | %s | %s |\n" % (str(detail["type"]),
                                                           str(detail["expected"]),
                                                           str(detail["actual"]),
                                                           str(detail["target"]))
        return result
