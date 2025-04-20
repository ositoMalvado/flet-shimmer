# Introduction

FletShimmer for Flet.

## Examples

```
import flet as ft

from flet_shimmer import FletShimmer


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(

                ft.Container(height=150, width=300, alignment = ft.alignment.center, bgcolor=ft.Colors.PURPLE_200, content=FletShimmer(
                    tooltip="My new FletShimmer Control tooltip",
                    value = "My new FletShimmer Flet Control", 
                ),),

    )


ft.app(main)
```

## Classes

[FletShimmer](FletShimmer.md)


