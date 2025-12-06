<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    
    <xsl:key name="word-lookup" match="sent//w" use="@id"/>
    
    <xsl:output method="text" encoding="UTF-8"/>
    
    <xsl:template match="/parallel_corpus">
        <xsl:text>&#10;</xsl:text>
        <xsl:text>|  Greek Text   |  Lattimore Text | Alignment Link (IDs) |&#10;</xsl:text>
        <xsl:text>|---------------|-----------------|----------------------|&#10;</xsl:text>
        <xsl:apply-templates select="sent/linkGrp/link"/>
    </xsl:template>
    
    <xsl:template match="link">
        <xsl:variable name="xtarget" select="@xtarget"/>
        
        <xsl:variable name="source-ids" select="substring-before($xtarget, ';')"/>
        <xsl:variable name="target-ids" select="substring-after($xtarget, ';')"/>
        
        <xsl:variable name="source-words">
            <xsl:call-template name="get-words-from-ids">
                <xsl:with-param name="ids" select="$source-ids"/>
            </xsl:call-template>
        </xsl:variable>

        <xsl:variable name="target-words">
            <xsl:call-template name="get-words-from-ids">
                <xsl:with-param name="ids" select="$target-ids"/>
            </xsl:call-template>
        </xsl:variable>

        <xsl:text>| </xsl:text>
        <xsl:value-of select="normalize-space($source-words)"/>
        <xsl:text> | </xsl:text>
        <xsl:value-of select="normalize-space($target-words)"/>
        <xsl:text> | </xsl:text>
        <xsl:value-of select="$xtarget"/>
        <xsl:text> |&#10;</xsl:text>
    </xsl:template>

    <xsl:template name="get-words-from-ids">
        <xsl:param name="ids"/>
        
        <xsl:choose>
            <xsl:when test="not($ids)">
                <xsl:text>---</xsl:text>
            </xsl:when>
            <xsl:when test="contains($ids, ' ')">
                <xsl:variable name="current-id" select="substring-before($ids, ' ')"/>
                <xsl:value-of select="key('word-lookup', $current-id)"/>
                <xsl:text> </xsl:text>
                <xsl:call-template name="get-words-from-ids">
                    <xsl:with-param name="ids" select="substring-after($ids, ' ')"/>
                </xsl:call-template>
            </xsl:when>
            <xsl:otherwise>
                <xsl:value-of select="key('word-lookup', $ids)"/>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

</xsl:stylesheet>