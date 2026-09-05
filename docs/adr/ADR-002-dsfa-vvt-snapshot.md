# ADR-002: DSFA immer gegen einen VVT-Snapshot führen

Eine DSFA referenziert eine stabile Verarbeitungstätigkeits-ID und speichert
die konkrete VVT-Version sowie einen Snapshot. Ändert sich die Verarbeitung,
kann die alte Freigabe weiterhin nachvollzogen werden; gleichzeitig wird eine
Neubewertung für die neue Version erforderlich.

