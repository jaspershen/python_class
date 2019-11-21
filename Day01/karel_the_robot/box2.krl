# Find your way out of the box. Door on north side
#
DEFINE-NEW-INSTRUCTION turnright AS
  BEGIN 
    turnleft turnleft turnleft
  END

DEFINE-NEW-INSTRUCTION walk-to-wall AS
  WHILE front-is-clear DO move

DEFINE-NEW-INSTRUCTION walk-to-door AS
  WHILE left-is-blocked DO move

BEGIN
  WHILE not-facing-west DO turnleft
END

