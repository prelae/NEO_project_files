"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str
from datetime import datetime


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """
    # TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, designation = str , name = None, diameter = float, hazardous = False, approaches = [], **info):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        # TODO: Assign information from the arguments passed to the constructor
        # onto attributes named `designation`, `name`, `diameter`, and `hazardous`.
        # You should coerce these values to their appropriate data type and
        # handle any edge cases, such as a empty name being represented by `None`
        # and a missing diameter being represented by `float('nan')`.
        self.designation = designation
        self.name = name
        self.diameter = diameter
        self.hazardous = hazardous
        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self, _fullname = str):
        """Return a representation of the full name of this NEO."""
        # TODO: Use self.designation and self.name to build a fullname for this object. 
        if self.name != None:
            self._fullname = ' '.join([self.designation, self.name])
        else:
            self._fullname = self.designation
        return self._fullname 
    
    def __getitem__(self, index):
        return self.approaches[index]
        
    def __str__(self, fullname = str, hazardstr = str):
        """Return `str(self)`."""
        # TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        self.hazardstr = hazardstr
        if self.hazardous == True:
            self.hazardstr = '' 
        elif self.hazardous == False:
            self.hazardstr = 'not'
        else:
            self.hazardstr = 'unknown if it is'
       
        return f"NearEarthObject Full name={self.fullname}, has a diameter of diameter={self.diameter:.2f}, is {self.hazardstr} potentially hazardous" 

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.2f}, hazardous={self.hazardous!r})")
    
class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """
    # TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, designation = str, time = "1900-Jan-01 00:00", distance = float, velocity = float, neo = None, **info):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        # TODO: Assign information from the arguments passed to the constructor
        # onto attributes named `_designation`, `time`, `distance`, and `velocity`.
        # You should coerce these values to their appropriate data type and handle any edge cases.
        # The `cd_to_datetime` function will be useful.
        self.designation = designation
        self.time = cd_to_datetime(time)  # TODO: Use the cd_to_datetime function for this attribute.
        self.distance = distance
        self.velocity = velocity

        # Create an attribute for the referenced NEO, originally None.
        self.neo = neo
    
    @property
    def time_str(self, time):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        self.time = self.time
        # TODO: Use this object's `.time` attribute and the `datetime_to_str` function to
        # build a formatted representation of the approach time.
        # TODO: Use self.designation and self.name to build a fullname for this object.
        return self.time
    
    def __str__(self):
        """Return `str(self)`."""
        # TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examp
        return f"A close approach was recorded at time= {self.time}, by object {self.designation} at a distance= {self.distance:.2f}, with velocity= {self.velocity:.2f}, by neo= {self.neo}"
    
    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"CloseApproach(designation={self.designation!r}, time={self.time!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")