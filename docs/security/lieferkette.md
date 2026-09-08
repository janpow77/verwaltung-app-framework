# Lieferkette und SBOM

F-07/F-08: Für eine auslieferbare Anwendung nachvollziehen, was tatsächlich
gebaut und betrieben wird. Eine SBOM ist eine maschinenlesbare Stückliste,
kein Beweis für Schwachstellenfreiheit oder zulässige Lizenzierung.
Dieses Inhaltsrepo erzeugt keine fingierte Anwendungs-SBOM.

## Pro Release

1. Laufzeit- und Buildabhängigkeiten, transitive Pakete, Containerbasis,
   eingebettete Bibliotheken und ggf. Modelle getrennt erfassen. Manuell
   eingebrachte Dateien nicht auslassen. Lockfiles und unveränderliche
   Artefaktkennungen verwenden; Aktualisierungsweg festlegen.
2. Generator, genaue Version, Eingaben und Reproduktionsbefehl protokollieren.
   SBOM aus dem tatsächlichen Build erzeugen. Format und Schemafassung
   festlegen, etwa [CycloneDX 1.6](https://cyclonedx.org/docs/1.6/json/).
3. Gegen das ausgewählte Schema validieren und mit Lockfiles sowie gebautem
   Artefakt abgleichen. Lücken ausdrücklich dokumentieren, nicht mit erfundenen
   Versionen oder Lizenzen füllen. Prüflauf darf keinen unkontrollierten
   Fremdcode aus Abhängigkeiten ausführen.
4. Artefakt, Commit und SBOM über Digests verbinden. Erstellungszeit,
   Herkunft und gegebenenfalls Signatur samt Verifikation festhalten.
5. Komponenten auf bekannte Schwachstellen prüfen: Scanner-/Datenbankstand,
   Befund-ID, betroffene Version, Erreichbarkeit, Bewertung, Maßnahme und
   Nachtest dokumentieren. Fristen und Eskalationsregeln legt die zuständige
   Sicherheitsrolle fest. Risikoakzeptanz ist keine automatische KI-Ausgabe.
6. Nutzungsrechte und Hinweise anhand der tatsächlich enthaltenen Komponenten
   prüfen. SBOM und Scanberichte geschützt mit dem Release aufbewahren;
   internen Paketnamen nicht ungeprüft öffentlich zugänglich machen.

## Prüfung T-37

In isolierter Testumgebung eine bekannte Testabhängigkeit ändern: SBOM muss
Version und Abhängigkeitsbeziehung korrekt ändern. Falschen Artefaktdigest und
ungültiges Schema als negative Fälle ablehnen. Einen synthetischen
Schwachstellenbefund durch Bewertung, Korrektur und Nachtest verfolgen.
Kein absichtlich verwundbares Paket in Produktion installieren.

[SBOM-Nachweis](../../vorlagen/sbom.md) und
[Nutzungsrechte](../../vorlagen/nutzungsrechte.md) gehören ins Landing-Paket.
