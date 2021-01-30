1	Joda Time is like an iceberg, 9/10ths of it is invisible to user-code.
2	Many, perhaps most, applications will never need to see what's below the surface.
3	This document provides an introduction to the Joda-Time API for the average user, not for the would-be API developer.
4	The bulk of the text is devoted to code snippets that display the most common usage scenarios in which the library classes are used.
5	In particular, we cover the usage of the key DateTime, Interval, Duration and Period classes.
6	We finish with a look at the important topic of formatting and parsing and a few more advanced topics.
7	The most frequently used concept in Joda-Time is that of the instant.
8	An Instant is defined as a moment in the datetime continuum specified as a number of milliseconds from 1970-01-01T00:00Z.
9	This definition of milliseconds is consistent with that of the JDK in Date or Calendar.
10	Interoperating between the two APIs is thus simple.
11	Within Joda-Time an instant is represented by the ReadableInstant interface.
12	The main implementation of this interface, and the class that the average API user needs to be most familiar with, is DateTime.
13	DateTime is immutable - and once created the values do not change.
14	Thus, this class can safely be passed around and used in multiple threads without synchronization.
15	The millisecond instant can be converted to any date time field using a Chronology.
16	To assist with this, methods are provided on DateTime that act as getters for the most common date and time fields.
17	We discuss the chronology concept a litte further on in this overview.
18	A companion mutable class to DateTime is MutableDateTime.
19	Objects of this class can be modified and are not thread-safe.
20	Other implementations of ReadableInstant include Instant and DateMidnight.
21	The main API of DateTime has been kept small, limited to just get methods for each calendar field.
22	So, for instance, the 'day-of-year' calendar field would be retrieved by calling the getDayOfYear() method.
23	For a complete list of fields and their descriptions, see the field reference.
24	There is much more power available, however, through the use of what is termed a property.
25	Each calendar field is associated with such a property.
26	Thus, 'day-of-year', whose value is directly returned by the method getDayOfYear(), is also associated with the property returned by the dayOfYear() method.
27	The property class associated with DateTime is DateTime.Property.
28	Knowing the methods on the property is the secret to making the most of the API.
29	We have more to say on the usage of properties later in this document.
30	An Interval in Joda-Time represents an interval of time from one instant to another instant.
31	Both instants are fully specified instants in the datetime continuum, complete with time zone.
32	Intervals are implemented as half-open, which is to say that the start instant is inclusive but the end instant is exclusive.
33	The end is always greater than or equal to the start.
34	Both end-points are restricted to having the same chronology and the same time zone.
35	Two implementations are provided, Interval and MutableInterval, both are specializations of ReadableInterval.
36	A Duration in Joda-Time represents a duration of time measured in milliseconds.
37	The duration is often obtained from an interval.
38	Durations are a very simple concept, and the implementation is also simple.
39	They have no chronology or time zone, and consist solely of the millisecond duration.
40	Durations can be added to an instant, or to either end of an interval to change those objects.
41	In datetime maths you could say:
42	Currently, there is only one implementation of the ReadableDuration interface: Duration.
43	A Period in Joda-Time represents a period of time defined in terms of fields, for example, 3 years 5 months 2 days and 7 hours.
44	This differs from a duration in that it is inexact in terms of milliseconds.
45	A period can only be resolved to an exact number of milliseconds by specifying the instant (including chronology and time zone) it is relative to.
46	For example, consider a period of 1 month.
47	If you add this period to the 1st February (ISO) then you will get the 1st March.
48	If you add the same period to the 1st March you will get the 1st April.
49	But the duration added (in milliseconds) in these two cases is very different.
50	As a second example, consider adding 1 day at the daylight savings boundary.
51	If you use a period to do the addition then either 23 or 25 hours will be added as appropriate.
52	If you had created a duration equal to 24 hours, then you would end up with the wrong result.
53	Periods are implemented as a set of int fields.
54	The standard set of fields in a period are years, months, weeks, days, hours, minutes, seconds and millis.
55	The PeriodType class allows this set of fields to be restricted, for example to elimate weeks.
56	This is significant when converting a duration or interval to a period, as the calculation needs to know which period fields it should populate.
57	Methods exist on periods to obtain each field value.
58	Periods are not associated with either a chronology or a time zone.
59	Periods can be added to an instant, or to either end of an interval to change those objects.
60	In datetime maths you could say:
61	There are two implementations of the ReadablePeriod interface, Period and MutablePeriod.
62	The Joda-Time design is based around the Chronology.
63	It is a calculation engine that supports the complex rules for a calendar system.
64	It encapsulates the field objects, which are used on demand to split the absolute time instant into recognisable calendar fields like 'day-of-week'.
65	It is effectively a pluggable calendar system.
66	The actual calculations of the chronology are split between the Chronology class itself and the field classes - DateTimeField and DurationField.
67	Together, the subclasses of these three classes form the bulk of the code in the library.
68	Most users will never need to use or refer directly to the subclasses.
69	Instead, they will simply obtain the chronology and use it as a singleton, as follows:
70	Internally, all the chronology, field, etc. classes are maintained as singletons.
71	Thus there is an initial setup cost when using Joda-Time, but after that only the main API instance classes (DateTime, Interval, Period, etc.) have creation and garbage collector costs.
72	Although the Chronology is key to the design, it is not key to using the API !!
73	For most applications, the Chronology can be ignored as it will default to the ISOChronology.
74	This is suitable for most uses.
75	You would change it if you need accurate dates before October 15, 1582, or whenever the Julian calendar ceased in the territory you're interested in).
76	You'd also change it if you need a specific calendar like the Coptic calendar illustrated earlier.
77	As you have seen, Joda-Time defines a number of new interfaces which are visible throughout the javadocs.
78	The most important is ReadableInstant which currently has 4 implementations.
79	Other significant interfaces include ReadableInterval and ReadablePeriod.
80	These are currently used as generalizations for a value-only and a mutable class, respectively.
81	An important point to mention here is that the Joda interfaces are used differently than, for instance, the JDK Collections Framework interfaces.
82	When working with a Collections interface, such as List or Map you will normally hold your variable as a type of List or Map, only referencing the concrete class when you create the object.
83	For maximum flexibility however, you might choose to declare your method parameters using the Joda-Time interface.
84	A method on the interface can obtain the concrete class for use within the method.
85	A datetime object is created by using a DateTime constructor.
86	The default constructor is used as follows
87	To create a datetime object representing a specific date and time, you may use an initialization string:
88	DateTime also provides other constructors to create a specific date and time using a variety of standard fields.
89	This also permits the use of any calendar and timezone.
90	The DateTime class has a constructor which takes an Object as input.
91	In particular this constructor can be passed a JDK Date, JDK Calendar or JDK GregorianCalendar (It also accepts an ISO8601 formatted String, or Long object representing milliseconds).
92	This is one half of the interoperability with the JDK.
93	The other half of interoperability with JDK is provided by DateTime methods which return JDK objects.
94	Thus inter-conversion between Joda DateTime and JDK Date can be performed as follows
95	Similarly, for JDK Calendar:
96	and JDK GregorianCalendar:
97	The separation of the calculation of calendar fields (DateTimeField) from the representation of the calendar instant (DateTime) makes for a powerful and flexible API.
98	The connection between the two is maintained by the property (DateTime.Property) which provides access to the field.
99	For instance, the direct way to get the day of week for a particular DateTime, involves calling the method
100	The direct methods are fine for simple usage, but more flexibility can be achieved via the property/field mechanism.
101	The day of week property is obtained by
102	Of course, the original integer value of the field is still accessible as
103	In practice, one would not actually create the intermediate pDoW variable.
104	The code is easier to read if the methods are called on anonymous intermediate objects.
105	Thus, for example,
106	Note: For the single case of getting the numerical value of a field, we recommend using the get method on the main DateTime object as it is more efficient.
107	The DateTime implementation provides a complete list of standard calendar fields:
108	As you would expect, all the methods we showed above in the day-of-week example can be applied to any of these properties.
109	For example, to extract the standard month, day and year fields from a datetime, we can write
110	Another set of properties access fields representing intra-day durations for time calculations.
111	Thus to compute the hours, minutes and seconds of the instant represented by a DateTime, we would write
112	DateTime objects have value semantics, and cannot be modified after construction (they are immutable).
113	Therefore, most simple manipulation of a datetime object involves construction of a new datetime as a modified copy of the original.
114	WARNING: A common mistake to make with immutable classes is to forget to assign the result to a variable.
115	Remember that calling an add or set method on an immtable object has no effect on that object - only the result is updated.
116	One way to do this is to use methods on properties.
117	To return to our prior example, if we wish to modify the dt object by changing its day-of-week field to Monday we can do so by using the setCopy method of the property:
118	To add to a date you could use the addToCopy method.
119	Another means of accomplishing similar calculations is to use methods on the DateTime object itself.
120	Thus we could add 3 days to dt directly as follows:
121	The methods outlined above are suitable for simple calculations involving one or two fields.
122	In situations where multiple fields need to be modified, it is more efficient to create a mutable copy of the datetime, modify the copy and finally create a new value datetime.
123	DateTime comes with support for a couple of common timezone calculations.
124	For instance, if you want to get the local time in London at this very moment, you would do the following
125	There is also support for the reverse operation, i.e. to get the datetime (absolute millisecond) corresponding to the moment when London has the same local time as exists in the default time zone now.
126	This is done as follows
127	A set of all TimeZone ID strings (such as ",Europe/London",) may be obtained by calling DateTimeZone.getAvailableIDs().
128	A full list of available time zones is provided here.
129	The DateTime class also has one method for changing calendars.
130	This allows you to change the calendar for a given moment in time.
131	Thus if you want to get the datetime for the current time, but in the Buddhist Calendar, you would do
132	All printing and parsing is performed using a DateTimeFormatter object.
133	Given such an object fmt, parsing is performed as follows
134	Support for standard formats based on ISO8601 is provided by the ISODateTimeFormat class.
135	This provides a number of factory methods.
136	For example, if you wanted to use the ISO standard format for datetime, which is yyyy-MM-dd'T'HH:mm:ss.SSSZZ, you would initialize fmt as
137	If you need a custom formatter which can be described in terms of a format pattern, you can use the factory method provided by the DateTimeFormat class.
138	Thus to get a formatter for a 4 digit year, 2 digit month and 2 digit day of month, i.e. a format of yyyyMMdd you would do
139	You may need to print or parse in a particular Locale.
140	This is achieved by calling the withLocale method on a formatter, which returns another formatter based on the original.
141	Finally, if you have a format that is not easily represented by a pattern string, Joda Time architecture exposes a builder class that can be used to build a custom formatter which is programatically defined.
142	Thus if you wanted a formatter to print and parse dates of the form ",22-Jan-65",, you could do the following:
143	What is particularly interesting about this format is the two digit year.
144	Since the interpretation of a two digit year is ambiguous, the appendTwoDigitYear takes an extra parameter that defines the 100 year range of the two digits, by specifying the mid point of the range.
145	In this example the range will be (1956 - 50) = 1906, to (1956 + 49) = 2005.
146	Thus 04 will be 2004 but 07 will be 1907.
147	This kind of conversion is not possible with ordinary format strings, highlighting the power of the Joda time formatting architecture.
148	To simplify the access to the formatter architecture, methods have been provided on the datetime classes such as DateTime.
149	Joda-Time allows you to change the current time.
150	All methods that get the current time are indirected via DateTimeUtils.
151	This allows the current time to be changed, which can be very useful for testing.
152	The constructors on each major concrete class in the API take an Object as a parameter.
153	This is passed to the converter subsystem which is responsible for converting the object to one acceptable to Joda-Time.
154	For example, the converters can convert a JDK Date object to a DateTime.
155	If required, you can add your own converters to those supplied in Joda-Time.
156	Joda-Time includes hooks into the standard JDK security scheme for sensitive changes.
157	These include changing the time zone handler, changing the current time and changing the converters.
158	See JodaTimePermission for details.
