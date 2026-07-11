%global tl_name bibleref-mouth
%global tl_revision 25527

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Consistent formatting of Bible references
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bibleref-mouth
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-mouth.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-mouth.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-mouth.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows Bible references to be formatted in a consistent way.
It is similar to the bibleref package, except that the formatting macros
are all purely expandable -- that is, they are all implemented in TeX's
mouth. This means that they can be used in any expandable context, such
as an argument to a \url command.

