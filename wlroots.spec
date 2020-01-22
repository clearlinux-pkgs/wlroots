#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wlroots
Version  : 0.9.1
Release  : 3
URL      : https://github.com/swaywm/wlroots/archive/0.9.1/wlroots-0.9.1.tar.gz
Source0  : https://github.com/swaywm/wlroots/archive/0.9.1/wlroots-0.9.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 MIT
Requires: wlroots-lib = %{version}-%{release}
Requires: wlroots-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(freerdp2)
BuildRequires : pkgconfig(libavcodec)
BuildRequires : pkgconfig(libavformat)
BuildRequires : pkgconfig(libavutil)
BuildRequires : pkgconfig(libcap)
BuildRequires : pkgconfig(libinput)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(wayland-server)
BuildRequires : pkgconfig(xkbcommon)

%description
# wlroots
Pluggable, composable, unopinionated modules for building a
[Wayland](http://wayland.freedesktop.org/) compositor; or about 50,000 lines of
code you were going to write anyway.

%package dev
Summary: dev components for the wlroots package.
Group: Development
Requires: wlroots-lib = %{version}-%{release}
Provides: wlroots-devel = %{version}-%{release}
Requires: wlroots = %{version}-%{release}

%description dev
dev components for the wlroots package.


%package lib
Summary: lib components for the wlroots package.
Group: Libraries
Requires: wlroots-license = %{version}-%{release}

%description lib
lib components for the wlroots package.


%package license
Summary: license components for the wlroots package.
Group: Default

%description license
license components for the wlroots package.


%prep
%setup -q -n wlroots-0.9.1
cd %{_builddir}/wlroots-0.9.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579733226
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/wlroots
cp %{_builddir}/wlroots-0.9.1/LICENSE %{buildroot}/usr/share/package-licenses/wlroots/cf7d4b8dccadb7713df91a14a5d9f5b53f493f3c
cp %{_builddir}/wlroots-0.9.1/tinywl/LICENSE %{buildroot}/usr/share/package-licenses/wlroots/df855b408256fed71fe29eb1382d03841508d0f2
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/wlr/backend.h
/usr/include/wlr/backend/drm.h
/usr/include/wlr/backend/headless.h
/usr/include/wlr/backend/interface.h
/usr/include/wlr/backend/libinput.h
/usr/include/wlr/backend/multi.h
/usr/include/wlr/backend/noop.h
/usr/include/wlr/backend/rdp.h
/usr/include/wlr/backend/session.h
/usr/include/wlr/backend/session/interface.h
/usr/include/wlr/backend/wayland.h
/usr/include/wlr/backend/x11.h
/usr/include/wlr/config.h
/usr/include/wlr/interfaces/wlr_input_device.h
/usr/include/wlr/interfaces/wlr_keyboard.h
/usr/include/wlr/interfaces/wlr_output.h
/usr/include/wlr/interfaces/wlr_pointer.h
/usr/include/wlr/interfaces/wlr_switch.h
/usr/include/wlr/interfaces/wlr_tablet_pad.h
/usr/include/wlr/interfaces/wlr_tablet_tool.h
/usr/include/wlr/interfaces/wlr_touch.h
/usr/include/wlr/render/dmabuf.h
/usr/include/wlr/render/drm_format_set.h
/usr/include/wlr/render/egl.h
/usr/include/wlr/render/gles2.h
/usr/include/wlr/render/interface.h
/usr/include/wlr/render/wlr_renderer.h
/usr/include/wlr/render/wlr_texture.h
/usr/include/wlr/types/wlr_box.h
/usr/include/wlr/types/wlr_buffer.h
/usr/include/wlr/types/wlr_compositor.h
/usr/include/wlr/types/wlr_cursor.h
/usr/include/wlr/types/wlr_data_control_v1.h
/usr/include/wlr/types/wlr_data_device.h
/usr/include/wlr/types/wlr_export_dmabuf_v1.h
/usr/include/wlr/types/wlr_foreign_toplevel_management_v1.h
/usr/include/wlr/types/wlr_fullscreen_shell_v1.h
/usr/include/wlr/types/wlr_gamma_control_v1.h
/usr/include/wlr/types/wlr_gtk_primary_selection.h
/usr/include/wlr/types/wlr_idle.h
/usr/include/wlr/types/wlr_idle_inhibit_v1.h
/usr/include/wlr/types/wlr_input_device.h
/usr/include/wlr/types/wlr_input_inhibitor.h
/usr/include/wlr/types/wlr_input_method_v2.h
/usr/include/wlr/types/wlr_keyboard.h
/usr/include/wlr/types/wlr_keyboard_group.h
/usr/include/wlr/types/wlr_layer_shell_v1.h
/usr/include/wlr/types/wlr_linux_dmabuf_v1.h
/usr/include/wlr/types/wlr_list.h
/usr/include/wlr/types/wlr_matrix.h
/usr/include/wlr/types/wlr_output.h
/usr/include/wlr/types/wlr_output_damage.h
/usr/include/wlr/types/wlr_output_layout.h
/usr/include/wlr/types/wlr_output_management_v1.h
/usr/include/wlr/types/wlr_pointer.h
/usr/include/wlr/types/wlr_pointer_constraints_v1.h
/usr/include/wlr/types/wlr_pointer_gestures_v1.h
/usr/include/wlr/types/wlr_presentation_time.h
/usr/include/wlr/types/wlr_primary_selection.h
/usr/include/wlr/types/wlr_primary_selection_v1.h
/usr/include/wlr/types/wlr_region.h
/usr/include/wlr/types/wlr_relative_pointer_v1.h
/usr/include/wlr/types/wlr_screencopy_v1.h
/usr/include/wlr/types/wlr_seat.h
/usr/include/wlr/types/wlr_server_decoration.h
/usr/include/wlr/types/wlr_surface.h
/usr/include/wlr/types/wlr_switch.h
/usr/include/wlr/types/wlr_tablet_pad.h
/usr/include/wlr/types/wlr_tablet_tool.h
/usr/include/wlr/types/wlr_tablet_v2.h
/usr/include/wlr/types/wlr_text_input_v3.h
/usr/include/wlr/types/wlr_touch.h
/usr/include/wlr/types/wlr_virtual_keyboard_v1.h
/usr/include/wlr/types/wlr_virtual_pointer_v1.h
/usr/include/wlr/types/wlr_xcursor_manager.h
/usr/include/wlr/types/wlr_xdg_decoration_v1.h
/usr/include/wlr/types/wlr_xdg_output_v1.h
/usr/include/wlr/types/wlr_xdg_shell.h
/usr/include/wlr/types/wlr_xdg_shell_v6.h
/usr/include/wlr/util/edges.h
/usr/include/wlr/util/log.h
/usr/include/wlr/util/region.h
/usr/include/wlr/version.h
/usr/include/wlr/xcursor.h
/usr/include/wlr/xwayland.h
/usr/lib64/libwlroots.so
/usr/lib64/pkgconfig/wlroots.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libwlroots.so.4
/usr/lib64/libwlroots.so.4.8.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/wlroots/cf7d4b8dccadb7713df91a14a5d9f5b53f493f3c
/usr/share/package-licenses/wlroots/df855b408256fed71fe29eb1382d03841508d0f2
