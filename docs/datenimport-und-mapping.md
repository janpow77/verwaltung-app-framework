# Datenimport, semantisches Mapping und Transformation

Dieses Dokument konkretisiert F-16.

## Grundsatz

Anwendungen, die strukturierte Daten aus fremden Systemen übernehmen, dürfen nicht voraussetzen, dass Quellspalten oder Tabellen bereits dem internen Fachmodell entsprechen. Import und Mapping werden als nachvollziehbarer eigener Schritt behandelt.

## Importprofil

Ein Importprofil dokumentiert mindestens:

- Quellformat und ggf. Tabellen/Blätter,
- erkannte Quellfelder,
- Zielobjekte und Zielfelder,
- Datentypen,
- Pflichtfelder,
- Transformationsregeln,
- Schlüssel und Beziehungen,
- Validierungsregeln,
- Version des Mappings,
- Ersteller und Änderungszeit.

## Semantisches Mapping

Das Projekt kann ein fachliches Zielmodell mit semantischen Rollen definieren. Beispiel:

```text
source: "Rechnungsbetrag brutto"
target: "receipt.amount_gross"
datatype: decimal
currency: EUR
decimal_separator: ","
thousands_separator: "."
```

Automatische oder KI-gestützte Zuordnungsvorschläge sind zulässig, müssen aber als Vorschlag gekennzeichnet sein und vor produktiver Nutzung nach den Projektregeln bestätigt werden.

## Transformationen

Mindestens zu berücksichtigen sind, soweit relevant:

- Datums- und Zeitformate,
- Dezimal-/Tausendertrennzeichen,
- Währungen,
- Einheiten,
- Zeichencodierung,
- normalisierte IDs,
- Wertelisten/Enums,
- Join-/Beziehungsregeln zwischen mehreren Dateien oder Tabellen.

Transformationen müssen deterministisch und versioniert sein. Freie, nicht dokumentierte Handkorrekturen während des Imports sind zu vermeiden oder als Änderung zu protokollieren.

## Vorschau und Validierung

Vor einer endgültigen Übernahme soll eine Vorschau ermöglichen:

- Quellwert,
- transformierten Wert,
- Zielfeld,
- Warnungen/Fehler.

Die Anwendung unterscheidet mindestens zwischen blockierenden Fehlern und Warnungen. Der Nutzer darf einen fehlerhaften Import nicht als erfolgreich missverstehen.

## Nachvollziehbarkeit

Für einen Importlauf werden soweit erforderlich gespeichert:

- Importprofil-/Mapping-Version,
- Quellfingerabdruck,
- Zeitpunkt,
- auslösende Person,
- Anzahl gelesener, übernommener, verworfener und fehlerhafter Zeilen,
- relevante Warnungen,
- Ergebnisfingerabdruck bzw. Zielversion.

## Mapping-Versionen

Änderungen eines produktiv genutzten Mappings erzeugen eine neue Version. Alte Importe bleiben ihrer damaligen Mapping-Version zugeordnet. Ein Mapping-Diff soll mindestens Änderungen an Feldzuordnungen, Datentypen, Transformationen und Beziehungen zeigen können.

## Prüfnachweise

Mindestens zu testen sind:

- vertauschte oder fehlende Quellspalten,
- ungültige Datums-/Zahlenformate,
- mehrere Tabellen mit Beziehungen,
- Änderung einer Mapping-Version ohne Veränderung historischer Importe,
- reproduzierbarer erneuter Import desselben Inputs mit derselben Mapping-Version,
- keine Einsicht in Mapping- oder Quelldaten eines fremden Mandanten.
