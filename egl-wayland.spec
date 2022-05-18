%global major 1
%define libname %mklibname nvidia-egl-wayland %major
%define devname %mklibname -d nvidia-egl-wayland
%global date %nil

Name:		egl-wayland
Version:	1.1.9
Release:	3
Group:		System/Libraries
Summary:	Wayland EGL External Platform library
License:	MIT1.1.5
URL:		https://github.com/NVIDIA/egl-wayland
# git archive --format=tar --prefix=egl-wayland-1.0.3-$(date +%Y%m%d)/ HEAD | xz -vf > egl-wayland-1.0.3-$(date +%Y%m%d).tar.xz
Source0:	%{name}-%{version}.tar.gz
Source1:	10_nvidia_wayland.json
Source2:	15_nvidia_gbm.json
Patch0:	https://github.com/NVIDIA/egl-wayland/commit/d4937adc5cd04ac7df98fc5616e40319fb52fdee.patch
Patch1:	https://github.com/NVIDIA/egl-wayland/commit/daab8546eca8428543a4d958a2c53fc747f70672.patch
Patch2:	https://github.com/NVIDIA/egl-wayland/commit/582b2d345abaa0e313cf16c902e602084ea59551.patch
Patch3:	https://github.com/NVIDIA/egl-wayland/commit/ddaa27209a8149c1960c70799c87151206401bbc.patch
BuildRequires:	meson
BuildRequires:	pkgconfig(eglexternalplatform) >= 1.0
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(wayland-server) >= 1.15.0
BuildRequires:	pkgconfig(wayland-client) >= 1.15.0
BuildRequires:	pkgconfig(wayland-scanner) >= 1.15.0
BuildRequires:	pkgconfig(wayland-protocols)
Requires:	%{libname} >= %{EVRD}
# Required for directory ownership
Requires:	libglvnd-egl

%description
%{summary}.

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries
Provides:	%{name}

%description -n %{libname}
%{summary}.

%package -n %{devname}
Summary:	Wayland EGL External Platform library development package
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Wayland EGL External Platform library development package.

%prep
%autosetup -p1
# remove Werror
sed -i '8d' src/meson.build

%build
%meson
%meson_build

%install
%meson_install
install -m 0755 -d %{buildroot}%{_datadir}/egl/egl_external_platform.d/
install -pm 0644 %{SOURCE1} %{SOURCE2} %{buildroot}%{_datadir}/egl/egl_external_platform.d/
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files

%files -n %{libname}
%doc README.md
%license COPYING
%{_libdir}/*.so.%{major}*
%{_datadir}/egl/egl_external_platform.d/10_nvidia_wayland.json
%{_datadir}/egl/egl_external_platform.d/15_nvidia_gbm.json

%files -n %{devname}
%{_libdir}/libnvidia-egl-wayland.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/pkgconfig/*.pc
%{_datadir}/wayland-eglstream/
