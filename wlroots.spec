#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v20
# autospec commit: f35655a
#
Name     : wlroots
Version  : 0.18.1
Release  : 36
URL      : https://gitlab.freedesktop.org/wlroots/wlroots/-/archive/0.18.1/wlroots-0.18.1.tar.gz
Source0  : https://gitlab.freedesktop.org/wlroots/wlroots/-/archive/0.18.1/wlroots-0.18.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 MIT
Requires: wlroots-license = %{version}-%{release}
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : buildreq-meson
BuildRequires : cairo-dev
BuildRequires : clr-hardware-files
BuildRequires : glslang-bin
BuildRequires : lcms2-dev
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(libavcodec)
BuildRequires : pkgconfig(libavformat)
BuildRequires : pkgconfig(libavutil)
BuildRequires : pkgconfig(libcap)
BuildRequires : pkgconfig(libdisplay-info)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libinput)
BuildRequires : pkgconfig(libliftoff)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libseat)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(wayland-server)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : systemd-dev
BuildRequires : xwayland
BuildRequires : xwayland-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# wlroots
Pluggable, composable, unopinionated modules for building a [Wayland]
compositor; or about 60,000 lines of code you were going to write anyway.

%package dev
Summary: dev components for the wlroots package.
Group: Development
Provides: wlroots-devel = %{version}-%{release}
Requires: wlroots = %{version}-%{release}

%description dev
dev components for the wlroots package.


%package license
Summary: license components for the wlroots package.
Group: Default

%description license
license components for the wlroots package.


%prep
%setup -q -n wlroots-0.18.1
cd %{_builddir}/wlroots-0.18.1
pushd ..
cp -a wlroots-0.18.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1728942055
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/wlroots
cp %{_builddir}/wlroots-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/wlroots/339d3e8d1d88715f085ca4f5ae5a843725e0535e || :
cp %{_builddir}/wlroots-%{version}/tinywl/LICENSE %{buildroot}/usr/share/package-licenses/wlroots/df855b408256fed71fe29eb1382d03841508d0f2 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/V3/usr/lib64/libwlroots-0.18.so
/usr/include/wlroots-0.18/wlr/backend.h
/usr/include/wlroots-0.18/wlr/backend/drm.h
/usr/include/wlroots-0.18/wlr/backend/headless.h
/usr/include/wlroots-0.18/wlr/backend/interface.h
/usr/include/wlroots-0.18/wlr/backend/libinput.h
/usr/include/wlroots-0.18/wlr/backend/multi.h
/usr/include/wlroots-0.18/wlr/backend/session.h
/usr/include/wlroots-0.18/wlr/backend/wayland.h
/usr/include/wlroots-0.18/wlr/backend/x11.h
/usr/include/wlroots-0.18/wlr/config.h
/usr/include/wlroots-0.18/wlr/interfaces/wlr_buffer.h
/usr/include/wlroots-0.18/wlr/interfaces/wlr_keyboard.h
/usr/include/wlroots-0.18/wlr/interfaces/wlr_output.h
/usr/include/wlroots-0.18/wlr/interfaces/wlr_pointer.h
/usr/include/wlroots-0.18/wlr/interfaces/wlr_switch.h
/usr/include/wlroots-0.18/wlr/interfaces/wlr_tablet_pad.h
/usr/include/wlroots-0.18/wlr/interfaces/wlr_tablet_tool.h
/usr/include/wlroots-0.18/wlr/interfaces/wlr_touch.h
/usr/include/wlroots-0.18/wlr/render/allocator.h
/usr/include/wlroots-0.18/wlr/render/color.h
/usr/include/wlroots-0.18/wlr/render/dmabuf.h
/usr/include/wlroots-0.18/wlr/render/drm_format_set.h
/usr/include/wlroots-0.18/wlr/render/drm_syncobj.h
/usr/include/wlroots-0.18/wlr/render/egl.h
/usr/include/wlroots-0.18/wlr/render/gles2.h
/usr/include/wlroots-0.18/wlr/render/interface.h
/usr/include/wlroots-0.18/wlr/render/pass.h
/usr/include/wlroots-0.18/wlr/render/pixman.h
/usr/include/wlroots-0.18/wlr/render/swapchain.h
/usr/include/wlroots-0.18/wlr/render/vulkan.h
/usr/include/wlroots-0.18/wlr/render/wlr_renderer.h
/usr/include/wlroots-0.18/wlr/render/wlr_texture.h
/usr/include/wlroots-0.18/wlr/types/wlr_alpha_modifier_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_buffer.h
/usr/include/wlroots-0.18/wlr/types/wlr_compositor.h
/usr/include/wlroots-0.18/wlr/types/wlr_content_type_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_cursor.h
/usr/include/wlroots-0.18/wlr/types/wlr_cursor_shape_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_damage_ring.h
/usr/include/wlroots-0.18/wlr/types/wlr_data_control_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_data_device.h
/usr/include/wlroots-0.18/wlr/types/wlr_drm.h
/usr/include/wlroots-0.18/wlr/types/wlr_drm_lease_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_export_dmabuf_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_ext_foreign_toplevel_list_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_foreign_toplevel_management_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_fractional_scale_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_fullscreen_shell_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_gamma_control_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_idle_inhibit_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_idle_notify_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_input_device.h
/usr/include/wlroots-0.18/wlr/types/wlr_input_method_v2.h
/usr/include/wlroots-0.18/wlr/types/wlr_keyboard.h
/usr/include/wlroots-0.18/wlr/types/wlr_keyboard_group.h
/usr/include/wlroots-0.18/wlr/types/wlr_keyboard_shortcuts_inhibit_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_layer_shell_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_linux_dmabuf_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_linux_drm_syncobj_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_matrix.h
/usr/include/wlroots-0.18/wlr/types/wlr_output.h
/usr/include/wlroots-0.18/wlr/types/wlr_output_layer.h
/usr/include/wlroots-0.18/wlr/types/wlr_output_layout.h
/usr/include/wlroots-0.18/wlr/types/wlr_output_management_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_output_power_management_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_output_swapchain_manager.h
/usr/include/wlroots-0.18/wlr/types/wlr_pointer.h
/usr/include/wlroots-0.18/wlr/types/wlr_pointer_constraints_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_pointer_gestures_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_presentation_time.h
/usr/include/wlroots-0.18/wlr/types/wlr_primary_selection.h
/usr/include/wlroots-0.18/wlr/types/wlr_primary_selection_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_region.h
/usr/include/wlroots-0.18/wlr/types/wlr_relative_pointer_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_scene.h
/usr/include/wlroots-0.18/wlr/types/wlr_screencopy_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_seat.h
/usr/include/wlroots-0.18/wlr/types/wlr_security_context_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_server_decoration.h
/usr/include/wlroots-0.18/wlr/types/wlr_session_lock_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_shm.h
/usr/include/wlroots-0.18/wlr/types/wlr_single_pixel_buffer_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_subcompositor.h
/usr/include/wlroots-0.18/wlr/types/wlr_switch.h
/usr/include/wlroots-0.18/wlr/types/wlr_tablet_pad.h
/usr/include/wlroots-0.18/wlr/types/wlr_tablet_tool.h
/usr/include/wlroots-0.18/wlr/types/wlr_tablet_v2.h
/usr/include/wlroots-0.18/wlr/types/wlr_tearing_control_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_text_input_v3.h
/usr/include/wlroots-0.18/wlr/types/wlr_touch.h
/usr/include/wlroots-0.18/wlr/types/wlr_transient_seat_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_viewporter.h
/usr/include/wlroots-0.18/wlr/types/wlr_virtual_keyboard_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_virtual_pointer_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_xcursor_manager.h
/usr/include/wlroots-0.18/wlr/types/wlr_xdg_activation_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_xdg_decoration_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_xdg_foreign_registry.h
/usr/include/wlroots-0.18/wlr/types/wlr_xdg_foreign_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_xdg_foreign_v2.h
/usr/include/wlroots-0.18/wlr/types/wlr_xdg_output_v1.h
/usr/include/wlroots-0.18/wlr/types/wlr_xdg_shell.h
/usr/include/wlroots-0.18/wlr/util/addon.h
/usr/include/wlroots-0.18/wlr/util/box.h
/usr/include/wlroots-0.18/wlr/util/edges.h
/usr/include/wlroots-0.18/wlr/util/log.h
/usr/include/wlroots-0.18/wlr/util/region.h
/usr/include/wlroots-0.18/wlr/util/transform.h
/usr/include/wlroots-0.18/wlr/version.h
/usr/include/wlroots-0.18/wlr/xcursor.h
/usr/include/wlroots-0.18/wlr/xwayland.h
/usr/include/wlroots-0.18/wlr/xwayland/server.h
/usr/include/wlroots-0.18/wlr/xwayland/shell.h
/usr/include/wlroots-0.18/wlr/xwayland/xwayland.h
/usr/lib64/libwlroots-0.18.so
/usr/lib64/pkgconfig/wlroots-0.18.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/wlroots/339d3e8d1d88715f085ca4f5ae5a843725e0535e
/usr/share/package-licenses/wlroots/df855b408256fed71fe29eb1382d03841508d0f2
