# Find your way out of the box. Door on north side.

DEFINE-NEW-INSTRUCTION turnright AS
# three lefts equals a right
  BEGIN
    turnleft turnleft turnleft
  END

BEGIN
  WHILE not-facing-west DO turnleft

  WHILE front-is-clear DO move

  turnright

  END
