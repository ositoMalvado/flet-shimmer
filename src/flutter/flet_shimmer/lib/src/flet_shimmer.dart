import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:shimmer/shimmer.dart';

class FletShimmerControl extends StatelessWidget with FletStoreMixin {
  final Control? parent;
  final Control control;
  final List<Control> children;
  final bool parentDisabled;
  final bool? parentAdaptive;
  final FletControlBackend backend;

  const FletShimmerControl(
      {super.key,
      required this.parent,
      required this.control,
      required this.children,
      required this.parentDisabled,
      required this.parentAdaptive,
      required this.backend});

  @override
  Widget build(BuildContext context) {
    var contentCtrls =
        children.where((c) => c.name == "content" && c.isVisible);

    bool? adaptive = control.attrBool("adaptive") ?? parentAdaptive;
    bool disabled = control.isDisabled || parentDisabled;
    Widget child = createControl(control, contentCtrls.first.id, disabled,
        parentAdaptive: adaptive);

    Color baseColor =
        control.attrColor("base_color", context) ?? Colors.grey.shade300;
    Color highlightColor =
        control.attrColor("highlight_color", context) ?? Colors.grey.shade100;
    final Duration duration =
        parseDuration(control, "duration") ?? Duration(milliseconds: 1500);
    bool enabled = control.attrBool("enabled") ?? true;
    String? shimmerDirectionJS =
        control.attrString("shimmer_direction") ?? "ltr";
    ShimmerDirection shimmerDirection = ShimmerDirection.ltr;
    switch (shimmerDirectionJS) {
      case "ltr":
        shimmerDirection = ShimmerDirection.ltr;
        break;
      case "rtl":
        shimmerDirection = ShimmerDirection.rtl;
        break;
      case "ttb":
        shimmerDirection = ShimmerDirection.ttb;
        break;
      case "btt":
        shimmerDirection = ShimmerDirection.btt;
        break;
    }
    double inclination = control.attrDouble("inclination") ?? 8.0;
    int loop = control.attrInt("loop") ?? 0;

    Widget myControl = Shimmer.fromColors(
      child: child,
      baseColor: baseColor,
      highlightColor: highlightColor,
      direction: shimmerDirection,
      inclination: inclination,
      period: duration,
      enabled: enabled,
      loop: loop,
    );

    return constrainedControl(context, myControl, parent, control);
  }
}
