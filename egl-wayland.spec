%global major 1
%define oldlibname %mklibname nvidia-egl-wayland %major
%define libname %mklibname nvidia-egl-wayland
%define devname %mklibname -d nvidia-egl-wayland
%global date %nil

Name:		egl-wayland
Version:	1.1.19
Release:	2
Group:		System/Libraries
Summary:	Wayland EGL External Platform library for nvidia GPUs
License:	MIT
URL:		https://github.com/NVIDIA/egl-wayland
Source0:	https://github.com/NVIDIA/egl-wayland/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	meson
BuildRequires:	pkgconfig(libdrm)
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
Provides:	%{name} = %{EVRD}
# Renamed after 6.0 2025/07/24
%rename %{oldlibname}

%description -n %{libname}
%{summary}.

%package -n %{devname}
Summary:	Wayland EGL External Platform library development package
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Wayland EGL External Platform library development package.

%files -n %{libname}
%doc README.md
%license COPYING
%{_libdir}/*.so.%{major}*
%{_datadir}/egl/egl_external_platform.d/10_nvidia_wayland.json

%files -n %{devname}
%{_libdir}/libnvidia-egl-wayland.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/pkgconfig/*.pc
%{_datadir}/wayland-eglstream/
