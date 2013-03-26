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
    <p><p><p><p>
    <table width="1000" border="0">
    <tr><td colspan="2" style="background-color:#ffff99">
    <h1 align="center">The powerful translator</h1>
    </td></tr>

    <tr valign="top">
    <td style=width:100px></td>
    <td valign="top" style="background-color:#EEEEEE">
    <form name="language" action="/" method="get">
    <select name="srclan">
    <option value="chinese">Chinese</option>
    <option value="english">English</option>
    </select>
    to    
    <select name="dstlan">
    <option value="english">English</option>
    <option value="chinese">Chinese</option>
    </select>
    <br /> <br />
    <input name="input" type="text"  size="25px"></input> 
    <input type="submit" value="translate"></input>
    </form>
    </td>
    </tr>
    </table>
    </body>
    </html>"""
