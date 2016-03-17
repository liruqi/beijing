<?php
require __DIR__ . '/vendor/autoload.php';

use PHPHtmlParser\Dom;

$dom = new Dom;
$dom->loadFromFile('audit_house_list/index.html');
$contents = $dom->find('tr');
echo count($contents); 

foreach ($contents as $content)
{
    // get the class attr
    $class = $content->getAttribute('class');

    // do something with the html
    $html = $content->innerHtml;

    // or refine the find some more
    $child   = $content->firstChild();
    $sibling = $child->nextSibling();
    echo $child;
}
