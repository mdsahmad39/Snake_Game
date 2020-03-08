""" The module contains logic of snake game"""


class Blockofsnake:
    """
    Attributes:
    -----------------
        snakehead : tuple(int, int)

        blocksize : tuple(int, int)

        snakecolour : tuple(int, int, int).

    Methods:
    -----------------
        get_coordinates(): returns coordinates of the head.

        get_size(): returns size value.

        get_colour():return colour value
    """

    def __init__(self, snakehead, blocksize, snakecolour):
        """
        Parameters:
            snakehead : (int,int)

            blocksize : (int, int)

            snakecolour : (int, int, int)

        """

        self.snakehead = snakehead
        self.blocksize = blocksize
        self.snakecolour = snakecolour

    def get_coordinates(self):
        """Returns : tuple(int, int)"""
        return self.snakehead

    def get_size(self):
        """Returns : tuple(int, int)"""
        return self.blocksize

    def get_colour(self):
        """Returns : tuple(int, int, int)"""
        return self.snakecolour


class Snake:
    """
    Attributes:
    -----------------
        blocksize : tuple(int, int)

        snakecolour : tuple(int, int, int)

    Methods:
    -----------------
        move_left():
            Moves the head to left direction.

        move_right():
            Moves the head to right direction.

        move_up():
            Moves the head upwards.

        move_down():
            Moves the head downwards.

        update_blocks():
            Other blocks follows.

        inside_bounds(left_up, right_down):
            Check whether the snake is inside the bounds or not.

        check_collision(left_up, right_down):
            Check collision with the given coordinates.

        check_collision_with_fruit(left_up, right_down):
            Check collision with coordinates of fruit.

        check_collision_with_self():
            Checks colllision with self.

        grow():
            Grows the snake by a block.

        grow_block():
            Add one more SnakeBlock.

        return_block():
            Grows the snake parts by adding one more Block
    """

    def __init__(self, snakehead, blocksize, snakecolour):
        """Initialize the snake.

        Parameters:

        snakecolour : (int, int, int)

        snakehead : (int, int)

        blocksize : (int, int)

        """
        self.blocksize = blocksize
        self.snakebody = []
        self.snake_blocksize = 1
        self.snakecolour = snakecolour
        self.snakehead = Blockofsnake(snakehead, self.blocksize, self.snakecolour)
        self.snakebody.append(self.snakehead)

    def move_left(self):
        """Moves the head to left direction."""
        (dir_x, dir_y) = (self.snakebody[0].snakehead[0], self.snakebody[0].snakehead[1])
        self.turn()
        self.snakebody[0].snakehead = (dir_x - self.blocksize[0], dir_y)

    def move_right(self):
        """Moves the head to right direction."""
        (dir_x, dir_y) = (self.snakebody[0].snakehead[0], self.snakebody[0].snakehead[1])
        self.turn()
        self.snakebody[0].snakehead = (dir_x + self.blocksize[0], dir_y)

    def move_up(self):
        """Moves the head upwards."""
        (dir_x, dir_y) = (self.snakebody[0].snakehead[0], self.snakebody[0].snakehead[1])
        self.turn()
        self.snakebody[0].snakehead = (dir_x, dir_y - self.blocksize[1])

    def move_down(self):
        """Moves the head downwards"""
        (dir_x, dir_y) = (self.snakebody[0].snakehead[0], self.snakebody[0].snakehead[1])
        self.turn()
        self.snakebody[0].snakehead = (dir_x, dir_y + self.blocksize[1])

    def turn(self):
        """changes the position"""
        for i in range(len(self.snakebody) - 1, 0, -1):
            self.snakebody[i].snakehead = self.snakebody[i - 1].snakehead

    def grow(self):
        """Increases the block by one"""
        self.snake_blocksize += 1
        self.snakebody.append(Blockofsnake(self.snakebody[-1].snakehead,
                                           self.blocksize, self.snakecolour))

    def check_collision(self, top_left, bottom_right):
        """ Checks collision with given arguments
        Parameters:
            top_left : tuple(int,int)
            bottom_right : tuple(int,int)
        """
        self.is_left_collision_snakehead(top_left, bottom_right)
        self.is_left_collision_blocksize(top_left, bottom_right)
        self.is_right_collision_snakehead(top_left, bottom_right)
        self.is_right_collision_blocksize(top_left, bottom_right)
        if top_left == self.snakebody[0].snakehead:
            return True
        return False

    def is_left_collision_snakehead(self, top_left, bottom_right):
        """Parameters:
            top_left : tuple(int,int)
            bottom_right : tuple(int,int)
        """
        for i in range(0, len(self.snakebody)):
            if (top_left[0] < self.snakebody[i].snakehead[0] < bottom_right[0]
                    and top_left[1] < self.snakebody[i].snakehead[1] < bottom_right[1]):
                return True

    def is_left_collision_blocksize(self, top_left, bottom_right):
        """Parameters:
            top_left : tuple(int,int)
            bottom_right : tuple(int,int)
        """
        for i in range(0, len(self.snakebody)):
            if (top_left[0] < self.snakebody[i].snakehead[0] + self.blocksize[0] < bottom_right[0]
                    and top_left[1] < self.snakebody[i].snakehead[1] < bottom_right[1]):
                return True

    def is_right_collision_snakehead(self, top_left, bottom_right):
        """Parameters:
            top_left : tuple(int,int)
            bottom_right : tuple(int,int)
        """
        for i in range(0, len(self.snakebody)):
            if (top_left[0] < self.snakebody[i].snakehead[0] < bottom_right[0]
                    and top_left[1] < self.snakebody[i].snakehead[1] +
                    self.blocksize[1] < bottom_right[1]):
                return True

    def is_right_collision_blocksize(self, top_left, bottom_right):
        """Parameters:
            top_left : tuple(int,int)
            bottom_right : tuple(int,int)
        """
        for i in range(0, len(self.snakebody)):
            if (top_left[0] < self.snakebody[i].snakehead[0] +
                    self.blocksize[0] < bottom_right[0] and
                    top_left[1] < self.snakebody[i].snakehead[1] +
                    self.blocksize[1] < bottom_right[1]):
                return True

    def inside_bounds(self, top_left, bottom_right):
        """
        Check whether snake is inside given bound region.

        Parameters:
            top_left : tuple(int,int)
            bottom_right : tuple(int,int)
        """
        if self.is_inside_top_left(top_left, bottom_right):
            if self.is_inside_bottom_right(top_left, bottom_right):
                return True
            else:
                return False
        else:
            return False

    def is_inside_top_left(self, top_left, bottom_right):
        """
        Check whether snake is inside left region.

        Parameters:
            top_left : tuple(int,int)
            bottom_right : tuple(int,int)
        """
        if (top_left[0] <= self.snakebody[0].snakehead[0] <= bottom_right[0] and
                top_left[1] <= self.snakebody[0].snakehead[1] <= bottom_right[1]):
            if (top_left[0] <= self.snakebody[0].snakehead[0] +
                    self.blocksize[0] <= bottom_right[0] and
                    top_left[1] <= self.snakebody[0].snakehead[1] <= bottom_right[1]):
                return True

        return False

    def is_inside_bottom_right(self, top_left, bottom_right):
        """
        Check whether snake is inside right region.

        Parameters:
            top_left : tuple(int,int)
            bottom_right : tuple(int,int)
        """
        if (top_left[0] <= self.snakebody[0].snakehead[0] <= bottom_right[0] and
                top_left[1] <= self.snakebody[0].snakehead[1] +
                self.blocksize[1] <= bottom_right[1]):
            if (top_left[0] <= self.snakebody[0].snakehead[0] +
                    self.blocksize[0] <= bottom_right[0] and
                    top_left[1] <= self.snakebody[0].snakehead[1] +
                    self.blocksize[1] <= bottom_right[1]):
                return True
        return False

    def check_collision_with_fruit(self, top_left, bottom_right):
        """
        checks whether the snake is in collision with fruit

        Parameters:
            top_left : tuple(int,int)
            bottom_right : tuple(int,int)
        """
        if (self.snakebody[0].snakehead == top_left and
                self.snakebody[0].blocksize[0] >= bottom_right[0] - top_left[0] and
                self.snakebody[0].blocksize[1] >= bottom_right[1] - top_left[1]):
            return True
        return False

    def check_collision_with_self(self):
        """
        checks whether the snake is in collision with self
        """
        for snake_part in self.snakebody[1:]:
            if self.snakebody[0].snakehead == snake_part.snakehead:
                return True
        return False

    def __iter__(self):
        """Iterator of the class"""
        self.loop = 0
        return self

    def return_snakebody(self):
        """Increasing the block"""
        self.loop += 1
        return self.snakebody[self.loop - 1]

    def __next__(self):
        """ Through blocks iteration """
        if self.loop < self.snake_blocksize:
            return self.return_snakebody()
        else:
            raise StopIteration
