<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:output method="html" indent="yes" encoding="UTF-8"/>

    <xsl:template match="/odyssey_variorum">
        <html>
        <head>
            <title>Odyssey Alignment (Revised Layout)</title>
            <style>
                body { font-family: sans-serif; }
                table { border-collapse: collapse; width: 100%; }
                th, td { border: 1px solid #ccc; padding: 10px; vertical-align: top; text-align: left; }
                th { background-color: #f0f0f0; }
                .line-id { 
                    font-weight: bold; 
                    background-color: #e0e0ff; 
                    padding: 2px 5px; 
                    margin-right: 5px; 
                    border-radius: 3px;
                }
                .token-word { 
                    cursor: pointer;
                    padding: 1px 0;
                    display: inline-block;
                }
                .highlight {
                    background-color: yellow;
                    font-weight: bold;
                }
                /* Style for the final Wilson line */
                .final-line {
                    text-align: right; /* Aligns the text content to the right */
                }
            </style>
            <script type="text/javascript">
                function highlightWords(token) {
                    // Remove existing highlights
                    document.querySelectorAll('.highlight').forEach(el => {
                        el.classList.remove('highlight');
                    });
                    
                    if (token) {
                        // Highlight all elements that share the same data-token
                        document.querySelectorAll(`[data-token="${token}"]`).forEach(el => {
                            el.classList.add('highlight');
                        });
                    }
                }
            </script>
        </head>
        <body>
            <h1>Homer's Odyssey: Opening Lines Variorum Alignment</h1>
            <p>Click any word to see its corresponding tokens highlighted across all versions.</p>
            <table>
                <thead>
                    <tr>
                        <th>Line</th>
                        <th>Greek</th>
                        <th>Lattimore Translation</th>
                        <th>Wilson Translation</th>
                    </tr>
                </thead>
                <tbody>
                    <xsl:apply-templates select="line[position() &lt;= 10]"/>
                    
                    <xsl:call-template name="final-wilson-line"/>
                </tbody>
            </table>
        </body>
        </html>
    </xsl:template>

    <xsl:template match="line">
        <tr>
            <td><xsl:value-of select="@line_id"/></td>
            
            <xsl:apply-templates select="version[@name='Greek']"/>
            
            <xsl:apply-templates select="version[@name='Lattimore']"/>
            
            <xsl:apply-templates select="version[@name='Wilson']"/>
        </tr>
    </xsl:template>

    <xsl:template name="final-wilson-line">
        <xsl:variable name="final-line" select="line[@line_id='11']"/>
        
        <xsl:if test="$final-line">
            <tr>
                <td></td>
                
                <td></td>
                
                <td></td>
                
                <td class="final-line">
                    <xsl:apply-templates select="$final-line/version[@name='Wilson']" mode="final"/>
                </td>
            </tr>
        </xsl:if>
    </xsl:template>

    <xsl:template match="version" mode="final">
        <span class="line-id">L<xsl:value-of select="../@line_id"/></span>
        <xsl:apply-templates select="word"/>
    </xsl:template>
    
    <xsl:template match="version">
        <span class="line-id">L<xsl:value-of select="../@line_id"/></span>
        <xsl:apply-templates select="word"/>
    </xsl:template>

    <xsl:template match="word">
        <span 
            class="token-word" 
            data-token-id="{@token_id}" 
            data-token="{@token}" 
            onclick="highlightWords(this.getAttribute('data-token'))"
            onmouseout="highlightWords('')"
        >
            <xsl:value-of select="."/>
        </span>
        <xsl:text> </xsl:text> </xsl:template>

</xsl:stylesheet>