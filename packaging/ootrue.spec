Name:           ootrue
Version:        0.1.0
Release:        1%{?dist}
Summary:        Instant zero-byte binary returning exit status 0 without runtime overhead.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ootrue
Source0:        ootrue-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ootrue is a sovereign, capability-bounded NO-OP SUCCESS written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ootrue
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ootrue-uninstall

%files
/usr/bin/ootrue
/usr/bin/ootrue-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
