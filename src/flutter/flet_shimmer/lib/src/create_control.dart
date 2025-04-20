import 'package:flet/flet.dart';

import 'flet_shimmer.dart';

CreateControlFactory createControl = (CreateControlArgs args) {
  switch (args.control.type) {
    case "flet_shimmer":
      return FletShimmerControl(
        parent: args.parent,
        control: args.control,
        children: args.children,
        parentAdaptive: args.parentAdaptive,
        parentDisabled: args.parentDisabled,
        backend: args.backend,
      );
    default:
      return null;
  }
};

void ensureInitialized() {
  // nothing to initialize
}
