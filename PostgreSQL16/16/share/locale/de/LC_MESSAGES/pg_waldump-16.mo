��    h      \  �   �      �  
   �     �  %   �  6   	  3   H	  P   |	  �   �	  P   W
  ?   �
  I   �
  =   2  A   p  6   �  �   �  D   �  �     >   �  �   �  B   y  C   �  ~           D   �     �     �  9   �  4   0  2   e  ;   �  @   �  R        h  :   �  %   �     �  �   �  P   x  Q   �  �         �  #        =  #   [  -     )   �     �     �       6   /  !   f     �     �     �  '   �  *     5   .  T   d  I   �  @     =   D     �  +   �     �  &   �  .   �      +     L  |   T     �  ;   �          /     J  5   g     �     �  >   �  A     <   N  <   �  $   �  '   �  *         @     a  \   }     �     �  ,     6   :  :   q  !   �  Q   �  "      .   C  #   r  $   �  0   �  $   �  /     A   A  $   �  	   �  �  �     k      w   %   �   <   �   <   �   s   7!  �   �!  u   E"  F   �"  R   #  D   U#  :   �#  >   �#  �   $  6   �$  �   +%  C   �%  �   &  J   �&  H   �&  �   >'     �'  B   �'     (     (  B   =(  ?   �(  E   �(  B   )  H   I)  Y   �)     �)  B   *  7   O*     �*  �   �*  R   )+  U   |+  �   �+      �,  1   �,  (   -  ,   C-  6   p-  3   �-     �-  $   �-  $   .  9   C.  +   }.  !   �.  %   �.  #   �.  2   /  0   H/  ?   y/  x   �/  ]   20  S   �0  P   �0  '   51  .   ]1     �1  0   �1  :   �1  #   2     %2  �   .2     �2  B   �2     3     03      O3  9   p3     �3     �3  A   �3  E   %4  I   k4  K   �4  "   5  +   $5  )   P5  &   z5     �5  c   �5      6  !   :6  2   \6  ;   �6  N   �6  &   7  T   A7  (   �7  0   �7  *   �7  '   8  <   C8     �8  7   �8  B   �8  #   9  	   ?9     S   _   N          >      
   0       X      g       U      6       e   $   9   E                   h   `   /   C   [   J      L   Y   H      =              ,   O       G              M              V   1   .   b   4       	   B       2           ?   -   \      7   5   +         ;   8      a   f       R   (   W      <          Q      c   Z       D   F       :      3                 "   @   #   )   %       K   &                  T   *   !         '   I      P   d   ^   ]                                       A           
Options:
 
Report bugs to <%s>.
   %s [OPTION]... [STARTSEG [ENDSEG]]
   --save-fullpage=DIR    save full page images to DIR
   -?, --help             show this help, then exit
   -B, --block=N          with --relation, only show records that modify block N
   -F, --fork=FORK        only show records that modify blocks in fork FORK;
                         valid names are main, fsm, vm, init
   -R, --relation=T/D/R   only show records that modify blocks in relation T/D/R
   -V, --version          output version information, then exit
   -b, --bkp-details      output detailed information about backup blocks
   -e, --end=RECPTR       stop reading at WAL location RECPTR
   -f, --follow           keep retrying after reaching end of WAL
   -n, --limit=N          number of records to display
   -p, --path=PATH        directory in which to find WAL segment files or a
                         directory with a ./pg_wal that contains such files
                         (default: current directory, ./pg_wal, $PGDATA/pg_wal)
   -q, --quiet            do not print any output, except for errors
   -r, --rmgr=RMGR        only show records generated by resource manager RMGR;
                         use --rmgr=list to list valid resource manager names
   -s, --start=RECPTR     start reading at WAL location RECPTR
   -t, --timeline=TLI     timeline from which to read WAL records
                         (default: 1 or the value used in STARTSEG)
   -w, --fullpage         only show records with a full page write
   -x, --xid=XID          only show records with transaction ID XID
   -z, --stats[=record]   show statistics instead of records
                         (optionally, show per-record statistics)
 %s %s decodes and displays PostgreSQL write-ahead logs for debugging.

 %s home page: <%s>
 %s must be in range %u..%u BKPBLOCK_HAS_DATA not set, but data length is %u at %X/%X BKPBLOCK_HAS_DATA set, but no data included at %X/%X BKPBLOCK_SAME_REL set but no previous rel at %X/%X BKPIMAGE_COMPRESSED set, but block image length %u at %X/%X BKPIMAGE_HAS_HOLE not set, but hole offset %u length %u at %X/%X BKPIMAGE_HAS_HOLE set, but hole offset %u length %u block image length %u at %X/%X ENDSEG %s is before STARTSEG %s Expecting "tablespace OID/database OID/relation filenode". Try "%s --help" for more information. Usage:
 WAL file is from different database system: WAL file database system identifier is %llu, pg_control database system identifier is %llu WAL file is from different database system: incorrect XLOG_BLCKSZ in page header WAL file is from different database system: incorrect segment size in page header WAL segment size must be a power of two between 1 MB and 1 GB, but the WAL file "%s" header specifies %d byte WAL segment size must be a power of two between 1 MB and 1 GB, but the WAL file "%s" header specifies %d bytes contrecord is requested by %X/%X could not access directory "%s": %m could not close file "%s": %m could not create directory "%s": %m could not decompress image at %X/%X, block %d could not find a valid record after %X/%X could not find any WAL file could not find file "%s": %m could not locate WAL file "%s" could not locate backup block with ID %d in WAL record could not open directory "%s": %m could not open file "%s" could not open file "%s": %m could not read file "%s": %m could not read file "%s": read %d of %d could not read from file %s, offset %d: %m could not read from file %s, offset %d: read %d of %d could not restore image at %X/%X compressed with %s not supported by build, block %d could not restore image at %X/%X compressed with unknown method, block %d could not restore image at %X/%X with invalid block %d specified could not restore image at %X/%X with invalid state, block %d could not write file "%s": %m custom resource manager "%s" does not exist detail:  directory "%s" exists but is not empty end WAL location %X/%X is not inside file "%s" error in WAL record at %X/%X: %s error:  first record is after %X/%X, at %X/%X, skipping over %u byte
 first record is after %X/%X, at %X/%X, skipping over %u bytes
 hint:  incorrect resource manager data checksum in record at %X/%X invalid WAL location: "%s" invalid block number: "%s" invalid block_id %u at %X/%X invalid contrecord length %u (expected %lld) at %X/%X invalid fork name: "%s" invalid fork number: %u invalid info bits %04X in WAL segment %s, LSN %X/%X, offset %u invalid magic number %04X in WAL segment %s, LSN %X/%X, offset %u invalid record length at %X/%X: expected at least %u, got %u invalid record offset at %X/%X: expected at least %u, got %u invalid relation specification: "%s" invalid resource manager ID %u at %X/%X invalid transaction ID specification: "%s" invalid value "%s" for option %s missing contrecord at %X/%X neither BKPIMAGE_HAS_HOLE nor BKPIMAGE_COMPRESSED set, but block image length is %u at %X/%X no arguments specified no start WAL location given option %s requires option %s to be specified out of memory while allocating a WAL reading processor out of memory while trying to decode a record of length %u out-of-order block_id %u at %X/%X out-of-sequence timeline ID %u (after %u) in WAL segment %s, LSN %X/%X, offset %u record length %u at %X/%X too long record with incorrect prev-link %X/%X at %X/%X record with invalid length at %X/%X resource manager "%s" does not exist start WAL location %X/%X is not inside file "%s" there is no contrecord flag at %X/%X too many command-line arguments (first is "%s") unexpected pageaddr %X/%X in WAL segment %s, LSN %X/%X, offset %u unrecognized value for option %s: %s warning:  Project-Id-Version: pg_waldump (PostgreSQL) 16
Report-Msgid-Bugs-To: pgsql-bugs@lists.postgresql.org
POT-Creation-Date: 2023-05-02 04:18+0000
PO-Revision-Date: 2023-11-08 21:40+0100
Last-Translator: Peter Eisentraut <peter@eisentraut.org>
Language-Team: German <pgsql-translators@postgresql.org>
Language: de
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Plural-Forms: nplurals=2; plural=n != 1;
 
Optionen:
 
Berichten Sie Fehler an <%s>.
   %s [OPTION]... [STARTSEG [ENDSEG]]
   --save-fullpage=VERZ   Full-Page-Images in VERZ speichern
   -?, --help             diese Hilfe anzeigen, dann beenden
   -B, --block=N          mit --relation, nur Datensätze zeigen, die Block N
                         modifizieren
   -F, --fork=FORK        nur Datensätze zeigen, die Blöcke in Fork FORK
                         modifizieren; gültige Werte sind main, fsm, vm, init
   -R, --relation=T/D/R   nur Datensätze zeigen, die Blöcke in Relation T/D/R
                         modifizieren
   -V, --version          Versionsinformationen anzeigen, dann beenden
   -b, --bkp-details      detaillierte Informationen über Backup-Blöcke ausgeben
   -e, --end=RECPTR       bei WAL-Position RECPTR zu lesen aufhören
   -f, --follow           am Ende des WAL weiter versuchen
   -n, --limit=N          Anzahl der anzuzeigenden Datensätze
   -p, --path=PATH        Verzeichnis mit den WAL-Segmentdateien oder Verzeichnis
                         mit ./pg_wal mit solchen Dateien (Vorgabe: aktuelles
                         Verzeichnis, ./pg_wal, $PGDATA/pg_wal)
   -q, --quiet            keine Ausgabe, außer Fehler
   -r, --rmgr=RMGR        nur Datensätze erzeugt von Resource-Manager RMGR zeigen;
                         --rmgr=list zeigt gültige Resource-Manager-Namen
   -s, --start=RECPTR     bei WAL-Position RECPTR zu lesen anfangen
   -t, --timeline=ZAHL    Zeitleiste aus der WAL-Einträge gelesen werden sollen
                         (Vorgabe: 1 oder der in STARTSEG verwendete Wert)
   -w, --fullpage         nur Datensätze mit einem Full-Page-Write zeigen
   -x, --xid=XID          nur Datensätze mit Transaktions-ID XID zeigen
   -z, --stats[=record]   Statistiken statt Datensätzen anzeigen
                         (optional Statistiken pro Datensatz zeigen)
 %s %s dekodiert und zeigt PostgreSQL-Write-Ahead-Logs zum Debuggen.

 %s Homepage: <%s>
 %s muss im Bereich %u..%u sein BKPBLOCK_HAS_DATA nicht gesetzt, aber Datenlänge ist %u bei %X/%X BKPBLOCK_HAS_DATA gesetzt, aber keine Daten enthalten bei %X/%X BKPBLOCK_SAME_REL gesetzt, aber keine vorangehende Relation bei %X/%X BKPIMAGE_COMPRESSED gesetzt, aber Block-Abbild-Länge %u bei %X/%X BKPIMAGE_HAS_HOLE nicht gesetzt, aber Loch Offset %u Länge %u bei %X/%X BKPIMAGE_HAS_HOLE gesetzt, aber Loch Offset %u Länge %u Block-Abbild-Länge %u bei %X/%X ENDSEG %s kommt vor STARTSEG %s Erwartet wurde »Tablespace-OID/Datenbank-OID/Relation-Filenode«. Versuchen Sie »%s --help« für weitere Informationen. Aufruf:
 WAL-Datei ist von einem anderen Datenbanksystem: Datenbanksystemidentifikator in WAL-Datei ist %llu, Datenbanksystemidentifikator in pg_control ist %llu WAL-Datei ist von einem anderen Datenbanksystem: falsche XLOG_BLCKSZ im Seitenkopf WAL-Datei ist von einem anderen Datenbanksystem: falsche Segmentgröße im Seitenkopf WAL-Segmentgröße muss eine Zweierpotenz zwischen 1 MB und 1 GB sein, aber der Kopf der WAL-Datei »%s« gibt %d Byte an WAL-Segmentgröße muss eine Zweierpotenz zwischen 1 MB und 1 GB sein, aber der Kopf der WAL-Datei »%s« gibt %d Bytes an Contrecord angefordert von %X/%X konnte nicht auf Verzeichnis »%s« zugreifen: %m konnte Datei »%s« nicht schließen: %m konnte Verzeichnis »%s« nicht erzeugen: %m konnte Abbild bei %X/%X nicht dekomprimieren, Block %d konnte keinen gültigen Datensatz nach %X/%X finden konnte keine WAL-Datei finden konnte Datei »%s« nicht finden: %m konnte WAL-Datei »%s« nicht finden konnte Backup-Block mit ID %d nicht im WAL-Eintrag finden konnte Verzeichnis »%s« nicht öffnen: %m konnte Datei »%s« nicht öffnen konnte Datei »%s« nicht öffnen: %m konnte Datei »%s« nicht lesen: %m konnte Datei »%s« nicht lesen: %d von %d gelesen konnte nicht aus Datei %s, Position %d lesen: %m konnte nicht aus Datei %s, Position %d lesen: %d von %d gelesen konnte Abbild bei %X/%X nicht wiederherstellen, komprimiert mit %s, nicht unterstützt von dieser Installation, Block %d konnte Abbild bei %X/%X nicht wiederherstellen, komprimiert mit unbekannter Methode, Block %d konnte Abbild bei %X/%X mit ungültigem angegebenen Block %d nicht wiederherstellen konnte Abbild mit ungültigem Zustand bei %X/%X nicht wiederherstellen, Block %d konnte Datei »%s« nicht schreiben: %m Custom-Resource-Manager »%s« existiert nicht Detail:  Verzeichnis »%s« existiert aber ist nicht leer WAL-Endposition %X/%X ist nicht innerhalb der Datei »%s« Fehler in WAL-Eintrag bei %X/%X: %s Fehler:  erster Datensatz kommt nach %X/%X, bei %X/%X, %u Byte wurde übersprungen
 erster Datensatz kommt nach %X/%X, bei %X/%X, %u Bytes wurden übersprungen
 Tipp:  ungültige Resource-Manager-Datenprüfsumme in Datensatz bei %X/%X ungültige WAL-Position: »%s« ungültige Blocknummer: »%s« ungültige block_id %u bei %X/%X ungültige Contrecord-Länge %u (erwartet %lld) bei %X/%X ungültiger Fork-Name: »%s« ungültige Fork-Nummer: %u ungültige Info-Bits %04X in WAL-Segment %s, LSN %X/%X, Offset %u ungültige magische Zahl %04X in WAL-Segment %s, LSN %X/%X, Offset %u ungültige Datensatzlänge bei %X/%X: mindestens %u erwartet, %u erhalten ungültiger Datensatz-Offset bei %X/%X: mindestens %u erwartet, %u erhalten ungültige Relationsangabe: »%s« ungültige Resource-Manager-ID %u bei %X/%X ungültige Transaktions-ID-Angabe: »%s« ungültiger Wert »%s« für Option %s Contrecord fehlt bei %X/%X weder BKPIMAGE_HAS_HOLE noch BKPIMAGE_COMPRESSED gesetzt, aber Block-Abbild-Länge ist %u bei %X/%X keine Argumente angegeben keine WAL-Startposition angegeben Option %s erfordert, dass Option %s angegeben wird Speicher aufgebraucht beim Anlegen eines WAL-Leseprozessors Speicher aufgebraucht beim Versuch einen Datensatz mit Länge %u zu dekodieren block_id %u außer der Reihe bei %X/%X Zeitleisten-ID %u außer der Reihe (nach %u) in WAL-Segment %s, LSN %X/%X, Offset %u Datensatzlänge %u bei %X/%X ist zu lang Datensatz mit falschem Prev-Link %X/%X bei %X/%X Datensatz mit ungültiger Länge bei %X/%X Resource-Manager »%s« existiert nicht WAL-Startposition %X/%X ist nicht innerhalb der Datei »%s« keine Contrecord-Flag bei %X/%X zu viele Kommandozeilenargumente (das erste ist »%s«) unerwartete Pageaddr %X/%X in WAL-Segment %s, LSN %X/%X, Offset %u unbekannter Wert für Option %s: %s Warnung:  