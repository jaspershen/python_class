DEFINE-NEW-INSTRUCTION walk-to-opening AS
  BEGIN
    IF front-is-clear THEN
      move
    IF right-is-clear THEN
      BEGIN
        turnleft
	turnleft
	turnleft
      END
    IF front-is-blocked THEN
      turnoff
  END

WHILE not-next-to-a-beeper DO
    walk-to-opening

