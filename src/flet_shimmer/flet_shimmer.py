from enum import Enum
from typing import Any, Optional, Union

from flet.core.constrained_control import ConstrainedControl
from flet.core.control import OptionalNumber, Control
from flet.core.types import ColorValue, ColorEnums, Duration


class ShimmerDirection(Enum):
    LEFT_TO_RIGHT: str = "ltr"
    RIGHT_TO_LEFT: str = "rtl"
    TOP_TO_BOTTOM: str = "ttb"
    BOTTOM_TO_TOP: str = "btt"


class Shimmer(ConstrainedControl):
    """
    A visual shimmer effect wrapper for Flet UI controls.

    FletShimmer overlays a shimmer animation on any child control, typically used to indicate loading content.
    It provides customization options such as base and highlight colors, direction of animation, shimmer angle,
    animation period, and looping behavior.

    Args:
        content (Control): The control to display with a shimmer effect overlay.
        base_color (Optional[ColorValue]): The base color of the shimmer animation. If not specified, a default color is used.
        highlight_color (Optional[ColorValue]): The highlight color used in the shimmer animation.
        direction (Optional[ShimmerDirection]): The direction of the shimmer animation (e.g., left-to-right, top-to-bottom).
        inclination (Optional[float]): The inclination angle of the shimmer in degrees. Default is 0 (horizontal shimmer).
        period (Optional[Duration]): The total duration of one shimmer cycle.
        enabled (Optional[bool]): Whether the shimmer effect is active. Defaults to True.
        loop (Optional[int]): The number of times to repeat the shimmer animation. Use 0 for infinite looping.

    Example:
        shimmer = FletShimmer(
            content=Text("Loading..."),
            base_color="#EEEEEE",
            highlight_color="#FFFFFF",
            direction=ShimmerDirection.LEFT_TO_RIGHT,
            inclination=15.0,
            period=Duration(seconds=2),
            enabled=True,
            loop=0,
        )
    """

    def __init__(
        self,
        #
        # FletShimmer specific
        #
        content: Control,
        base_color: Optional[ColorValue] = None,
        highlight_color: Optional[ColorValue] = None,
        direction: Optional[ShimmerDirection] = None,
        inclination: Optional[float] = None,
        period: Optional[Duration] = None,
        enabled: Optional[bool] = None,
        loop: Optional[int] = None,
        #
        # Control
        #
        opacity: OptionalNumber = None,
        tooltip: Optional[str] = None,
        visible: Optional[bool] = None,
        data: Any = None,
        #
        # ConstrainedControl
        #
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
    ):
        ConstrainedControl.__init__(
            self,
            tooltip=tooltip,
            opacity=opacity,
            visible=visible,
            data=data,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
        )
        self.content = content

        self.base_color = base_color
        self.highlight_color = highlight_color
        self.direction = direction
        self.inclination = inclination
        self.period = period
        self.enabled = enabled
        self.loop = loop

    def _get_control_name(self):
        return "flet_shimmer"

    # content
    @property
    def content(self) -> Control:
        return self.__content

    @content.setter
    def content(self, value: Control):
        self.__content = value

    def _get_children(self):
        children = []
        if self.__content is not None:
            self.__content._set_attr_internal("n", "content")
            children.append(self.__content)
        return children

    @property
    def base_color(self) -> Optional[ColorValue]:
        """Get the base color for the shimmer effect.
        
        The base color represents the starting color or background color
        of the shimmer animation.
        
        Returns:
            Optional[ColorValue]: The current base color value or None if not set
        """
        return self.__base_color

    @base_color.setter
    def base_color(self, value: Optional[ColorValue]):
        self.__base_color = value
        self._set_enum_attr("base_color", value, ColorEnums)

    @property
    def highlight_color(self) -> Optional[ColorValue]:
        """Get the highlight color for the shimmer effect.
        
        The highlight color represents the accent or shimmer color that
        animates across the base color during the effect.
        
        Returns:
            Optional[ColorValue]: The current highlight color value or None if not set
        """
        return self.__highlight_color

    @highlight_color.setter
    def highlight_color(self, value: Optional[ColorValue]):
        self.__highlight_color = value
        self._set_enum_attr("highlight_color", value, ColorEnums)

    @property
    def direction(self) -> Optional[ShimmerDirection]:
        """Get or set the shimmer direction.

        Returns:
            Optional[ShimmerDirection]: The current shimmer direction or None if not set

        Setter Args:
            value (Union[Optional[ShimmerDirection], Optional[str]]):
                The shimmer direction to set. Can be:
                - A ShimmerDirection enum value
                - A string value ("ltr", "rtl", "ttb", "btt")
                - None
        """
        return self.__direction

    @direction.setter
    def direction(self, value: Union[Optional[ShimmerDirection], Optional[str]]):
        if isinstance(value, ShimmerDirection):
            self.__direction = value
            self._set_attr("shimmer_direction", value.value)
        else:
            self.__direction = value
            self._set_attr("shimmer_direction", value)

    @property
    def inclination(self) -> Optional[float]:
        """Get or set the inclination angle in degrees.

        Returns:
            float: The current inclination value, or 0 if none is set

        Setter Args:
            value (Optional[float]): The inclination angle to set, must be between
                                    -22.5 and 22.5 degrees. If None, sets to 0.

        Raises:
            ValueError: If the value is outside the allowed range (-22.5 to 22.5 degrees)
        """
        return 0 if self.__inclination is None else self.__inclination

    @inclination.setter
    def inclination(self, value: Optional[float]):
        if value is None:
            self.__inclination = 0
        elif -22.5 <= value <= 22.5:
            self.__inclination = value
        else:
            raise ValueError("Inclination must be between -22.5 and 22.5 degrees")

        self._set_attr("inclination", self.__inclination)

    @property
    def period(self) -> Optional[Duration]:
        """Get or set the shimmer animation period.

        Returns:
            Optional[Duration]: The current period duration or None if not set

        Setter Args:
            value (Optional[Duration]):
                The period duration to set. Must be a Duration object or None.
                If None is provided, the period will be unset.
        """
        return self.__period

    @period.setter
    def period(self, value: Optional[Duration]):
        if value is not None:
            # Calculate total microseconds to check minimum duration
            total_microseconds = (
                value.microseconds
                + value.milliseconds * 1000
                + value.seconds * 1000000
                + value.minutes * 60 * 1000000
                + value.hours * 60 * 60 * 1000000
                + value.days * 24 * 60 * 60 * 1000000
            )

            if total_microseconds < 1:
                raise ValueError("Period duration must be at least 1 microsecond")

            self.__period = value
            self._set_attr_json(
                "duration",
                {
                    "microseconds": value.microseconds,
                    "milliseconds": value.milliseconds,
                    "seconds": value.seconds,
                    "minutes": value.minutes,
                    "hours": value.hours,
                    "days": value.days,
                },
            )
        else:
            self.__period = None
            self._set_attr_json("duration", None)

    @property
    def enabled(self) -> Optional[bool]:
        """Get or set whether the shimmer effect is enabled.

        Returns:
            Optional[bool]: True if the shimmer effect is enabled, False if disabled,
                            or None if not set

        Setter Args:
            value (Optional[bool]):
                Whether to enable the shimmer effect.
                Set to True to enable, False to disable, or None to clear the setting.
        """
        return self.__enabled

    @enabled.setter
    def enabled(self, value: Optional[bool]):
        self.__enabled = value
        self._set_attr("enabled", value)

    @property
    def loop(self) -> Optional[int]:
        """Get or set the number of times the shimmer animation should loop.

        Returns:
            Optional[int]: The current loop count or None if not set

        Setter Args:
            value (Optional[int]):
                The number of times the animation should loop.
                Set to 0 for infinite looping, a positive integer for a specific count,
                or None to clear the setting.
        """
        return self.__loop

    @loop.setter
    def loop(self, value: Optional[int]):
        if value is None:
            self.__loop = None
        elif isinstance(value, int) and value >= 0:
            self.__loop = value
        else:
            raise ValueError(
                "Loop value must be None, 0 (for infinite), or a positive integer"
            )

        self._set_attr("loop", self.__loop)
