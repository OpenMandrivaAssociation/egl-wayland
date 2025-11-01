%global major 1
%define oldlibname %mklibname nvidia-egl-wayland %major
%define libname %mklibname nvidia-egl-wayland
%define devname %mklibname -d nvidia-egl-wayland
%define lib32name %mklib32name nvidia-egl-wayland
%define dev32name %mklib32name -d nvidia-egl-wayland
%global date %nil

%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

Name:		egl-wayland
Version:	1.1.20
Release:	1
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
BuildRequires:	pkgconfig(libffi)
%if %{with compat32}
BuildRequires:	devel(libdrm)
BuildRequires:	devel(libEGL)
BuildRequires:	devel(libwayland-server)
BuildRequires:	devel(libwayland-client)
BuildRequires:	devel(libffi)
%endif
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

%package -n %{lib32name}
Summary:	%{summary} (32-bit)
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}

%description -n %{lib32name}
%{summary}.

%package -n %{dev32name}
Summary:	Wayland EGL External Platform library development package (32-bit)
Group:		Development/C
Requires:	%{devname} = %{EVRD}
Requires:	%{lib32name} = %{EVRD}

%description -n %{dev32name}
Wayland EGL External Platform library development package (32-bit).

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

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/*.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/*.so
%{_prefix}/lib/pkgconfig/*.pc
%endif
