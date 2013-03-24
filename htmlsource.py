""" HTML source  class.

Note: This module general dynimical html source wirted by Request Handler response.

Content: 
 -HtmlSource:  The base class 
 -HtmlSoucrxx: The class provides html source for "xx"lanaguage.

"""

class HtmlSource:
    """ HTML source base class.
    """
    pass

class HtmlSourceEn(HtmlSource):
    """ HTML source for english language class.
    """
    strHtmlHome = """\
    <html>
    <body>
    <table width="1000" border="0">
    <tr>
    <td ><h1 align="left">The powerful translator</h1></td>
    </tr>

    <tr valign="top">
    <td style=width:100px>left</td>
    <td valign="top">
    <form>
    <h1> Please Selected: </h1>
    <select name="Chinese">
    <option value="Chinese">Chinese</option>
    <option value="English">english</option>
    </select>
    </form>
    </td>
    </tr>

    </table>
    </body>
    </html>"""
